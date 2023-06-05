// https://projecteuler.net/problem=2

pub fn solution1(limit: i32) -> i32 {
    let mut total = 0;
    let (mut a, mut b) = (0, 1);
    while a <= limit {
        if a % 2 == 0 {
            total += a;
        }
        (a, b) = (b, a + b);
    }
    total
}

pub fn solve() {
    println!("{}", solution1(4000000));
}
