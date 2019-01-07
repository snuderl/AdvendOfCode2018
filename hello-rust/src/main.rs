//use std::collections::Vec;


fn main() {
    use std::time::Instant;
    let now = Instant::now();

    let mut list: Vec<usize> = Vec::new();
    list.push(3);
    list.push(7);

    let array = [9,3,9,6,0,1];
    let len = array.len();

    let mut p1: usize = 0;
    let mut p2: usize = 1;
    while true {
        let new = list[p1] + list[p2];
        if new >= 10 {
            list.push(new / 10);

            if list.len() >= len {
                let mut found = true;
                let idx = list.len() - len;
                for i in 0..len {
                    if list[idx + i] != array[i] {
                        found = false;
                        break;
                    }
                }

                if found {
                    break;
                }
            }

            list.push(new % 10);
            
        } else {
            list.push(new);
        }

        p1 = (p1 + list[p1] + 1) % list.len();
        p2 = (p2 + list[p2] + 1) % list.len();

        if list.len() >= len {
            let mut found = true;
            let idx = list.len() - len;
            for i in 0..len {
                if list[idx + i] != array[i] {
                    found = false;
                    break;
                }
            }

            if found {
                break;
            }
        }
    }

    println!("{}", list.len() - 5);

    let elapsed = now.elapsed();
    let sec = (elapsed.as_secs() as f64) + (elapsed.subsec_nanos() as f64 / 1000_000_000.0);
    println!("Seconds: {}", sec);
}
