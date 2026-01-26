class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());

        int minDiff = INT_MAX;
        int n = arr.size();

        // Step 1: Find minimum absolute difference
        for (int i = 0; i < n - 1; i++) {
            minDiff = min(minDiff, arr[i + 1] - arr[i]);
        }

        vector<vector<int>> result;

        // Step 2: Collect all pairs with minDiff
        for (int i = 0; i < n - 1; i++) {
            if (arr[i + 1] - arr[i] == minDiff) {
                result.push_back({arr[i], arr[i + 1]});
            }
        }

        return result;
    }
};