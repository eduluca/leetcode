#include <limits>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxp = 0;
        int lowest = 99999; //numeric_limits<int>::infinity();

        for (int i = 0; i < prices.size(); i++){
            lowest = min(lowest,prices[i]);
            maxp = max(maxp, prices[i] - lowest);
        }
        return maxp;
    }
};


/////////////////////// TEST //////////////////////////////
int main() {
    Solution solution;
    vector<int> prices = {7,1,5,3,6,4};

    int max_profit = solution.maxProfit(prices);

    cout << "Maximum profit: " << max_profit << endl;

    return 0;
}