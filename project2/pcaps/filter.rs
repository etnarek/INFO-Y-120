use std::io;
use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;
use std::collections::HashSet;

fn load_alexa() -> HashSet<String> {
    let mut alexa = HashSet::new();
    let f = match File::open("alexa.csv") {
        Ok(file) => file,
        Err(e) => {
            println!("Couldn't open alexa.csv : {}", e);
            return alexa;
        }
    };
    let file = BufReader::new(&f);
    for line in file.lines() {
        match line {
            Ok(l) => {
                let ll: Vec<&str> = l.split(',').collect();
                alexa.insert(ll[1].to_owned());
            }
            Err(_) => {}
        }
    }

    alexa
}

fn process(line: String, alexa: &HashSet<String>) {
    let l: Vec<&str> = line.split("\t").collect();
    let s = l[6].to_owned();
    let s_trim = s.trim_matches('"');
    if alexa.contains(s_trim) {
        return;
    }

    let max = s_trim.split('.').count() - 1;
    for i in 1..max {
        let ss: Vec<&str> = s_trim.splitn(i + 1, '.').collect();
        if alexa.contains(&ss[i..].join(".")) {
            return;
        }
    }
    println!("{}", line);
}


fn main() {
    eprintln!("Loading alexa");
    let alexa = load_alexa();
    eprintln!("Alexa loaded");

    let mut header = String::new();
    io::stdin().read_line(&mut header).unwrap();
    println!("{}", header.trim());

    let stdin = BufReader::new(io::stdin());
    for line in stdin.lines() {
        match line {
            Ok(l) => process(l, &alexa),
            Err(_) => {}
        }
    }
}
