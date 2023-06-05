// https://leetcode.com/problems/two-sum/

// impl Solution {
pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    use std::collections::HashMap;
    let mut looking_for: HashMap<i32, i32> = HashMap::new();

    for (i, num) in nums.iter().enumerate() {
        match looking_for.get(num) {
            None => looking_for.insert(target - num, i as i32),
            Some(&index) => return vec![index, i as i32 as i32],
        };
    }
    vec![]
}
// }
