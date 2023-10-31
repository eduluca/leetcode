#include <unordered_map>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> num_map;
        for (int i=0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (num_map.find(diff) != num_map.end()){
                return {num_map[diff], i};
            }
            num_map[nums[i]] = i;
        }
        return {};
    }       
};

//////////// TEST ////////////////////

int main() {
    Solution solution;
    vector<int> nums = {2,7,11,15};
    int target = 9;

    vector<int> result = solution.twoSum(nums, target);

    cout << "Indices: ";
    for (int i : result) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}