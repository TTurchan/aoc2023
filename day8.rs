use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashMap;

fn read_lines<P>(filename: P) -> io::Result<(String,HashMap<String,String>)>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    let buf_reader = io::BufReader::new(file);
    let mut lines_iter = buf_reader.lines();

    let first_line = lines_iter.next()
        .ok_or_else(|| io::Error::new(io::ErrorKind::NotFound, "No lines found in file"))? // Converts Option to Result
        .map_err(|e| e)?;
        
    let _ = lines_iter.next();
    let mut map: HashMap<String,String> = HashMap::new();
    for line_result in lines_iter{
        if let Ok(line) = line_result {
            let key = &line[..3];
            let value = &line[7..15];
            map.insert(key.to_string(),value.to_string());
        }

    }


    Ok((first_line,map))
}
fn main() {
    part_two();
    part_one();
}

fn part_two() {
    let file_path = "day8input.txt";
    println!("\n\nPart Two\n\n");
    match read_lines(file_path) {
        Ok((first_line, direction_map)) => {
            let mut keys: Vec<String> = Vec::new();
            for key in direction_map.keys() {

                if &key[2..3] == "A"{
                    keys.push(key.to_string());
                }
            }
            let mut dir_count = 0;
            let mut repetitions = Vec::new();
            let mut bases = Vec::new();
            for key in &mut keys{
                let mut rep_count = 0;
                dir_count = 0;
                while rep_count < 2{
                    for c in first_line.chars(){
                        dir_count = dir_count+1;
                        if let Some(string_ref) = direction_map.get(key){
                            if c == 'R'{
                                *key = string_ref[5..].to_string();
 
                            } else {
                                *key = string_ref[..3].to_string();
                            }
                        }
                            

                        if &key[2..3] == "Z"{
                            if rep_count == 0{
                                bases.push(dir_count);
                            } else {
                                repetitions.push(dir_count-bases[bases.len()-1]);
                            }
                            rep_count = rep_count +1;
                        }
                    }
                }
            }
            for base in &bases{
                println!("{}",base);
            }
            println!("");
            for cycle in &repetitions{
                println!("{}",cycle);
            }
            
        }
        Err(e) => println!("Error: {}", e),
    }
}
fn part_one() {
    let file_path = "day8input.txt";
    println!("\n\n\n\nPart One\n\n");
    match read_lines(file_path) {
        Ok((first_line, direction_map)) => {
            let mut curr_key = "AAA";
            let mut dir_count = 0;
            while curr_key != "ZZZ"{
                dir_count = dir_count+1;
                for c in first_line.chars(){
                    if let Some(string_ref) = direction_map.get(curr_key){
                        
                        if c == 'R'{
                            curr_key = &string_ref[5..];
                        } else {
                            curr_key = &string_ref[..3];
                        }
                    }
                }
            }
            println!("Count: {}", dir_count*first_line.len());
        }
        Err(e) => println!("Error: {}", e),
    }
    print!("\n\n\n");
}
