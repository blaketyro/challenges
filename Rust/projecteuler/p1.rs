// https://projecteuler.net/problem=1

// Looping solution
pub fn solution1(limit: i32) -> i32 {
    let mut total = 0;
    for i in 1..limit {
        if i % 3 == 0 || i % 5 == 0 {
            total += i;
        }
    }
    total
}

// Math solution
pub fn solution2(limit: i32) -> i32 {
    let n = limit - 1;
    let tri = |n: i32| n * (n + 1) / 2;
    let helper = |d: i32| d * tri(n / d);
    helper(3) + helper(5) - helper(15)
}

pub fn solve() {
    println!("{}", solution1(10));
    println!("{}", solution1(1000));
    println!("{}", solution2(10));
    println!("{}", solution2(1000));
}
