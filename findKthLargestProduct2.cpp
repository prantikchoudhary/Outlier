#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

long long findKthLargestProduct2(std::vector<int>& arr, int k) {
    int n = arr.size();
    if (n < 2 || k <= 0 || k > (long long)n * (n - 1) / 2) {
        return -1; // Invalid input
    }

    // Sort the array
    std::sort(arr.begin(), arr.end());

    // Estimate the minimum and maximum possible products
    long long min_product = std::min({(long long)arr[0] * arr[1],
                                      (long long)arr[0] * arr[n - 1],
                                      (long long)arr[n - 2] * arr[n - 1]});

    long long max_product = std::max({(long long)arr[0] * arr[1],
                                      (long long)arr[0] * arr[n - 1],
                                      (long long)arr[n - 2] * arr[n - 1]});

    // Function to count the number of products greater than or equal to 'mid'
    auto countGE = [&](long long mid) -> long long {
        long long count = 0;
        int left, right;

        // Count products where both numbers are positive
        left = 0;
        right = n - 1;
        while (left < right && arr[right] > 0) {
            while (left < right && arr[left] * (long long)arr[right] < mid) {
                left++;
            }
            count += right - left;
            right--;
            left = 0; // Reset left pointer
        }

        // Count products where both numbers are negative
        left = 0;
        right = n - 1;
        while (left < right && arr[left] < 0) {
            while (left < right && arr[left] * (long long)arr[right] < mid) {
                right--;
            }
            count += right - left;
            left++;
            right = n - 1; // Reset right pointer
        }

        // Count products involving zeros (if mid <= 0)
        int zero_count = std::count(arr.begin(), arr.end(), 0);
        if (zero_count > 0) {
            if (mid <= 0) {
                long long zero_pairs = (long long)zero_count * (n - zero_count)
                                       + (long long)zero_count * (zero_count - 1) / 2;
                count += zero_pairs;
            } else {
                // All products involving zero are zero, which is less than mid if mid > 0
                // So we don't add anything to count in this case
            }
        }

        // Count products where one number is negative and the other is positive
        int neg_count = std::lower_bound(arr.begin(), arr.end(), 0) - arr.begin();
        int pos_count = arr.end() - std::upper_bound(arr.begin(), arr.end(), 0);
        if (neg_count > 0 && pos_count > 0) {
            if (mid <= 0) {
                count += (long long)neg_count * pos_count;
            } else {
                // Count negative * positive products less than mid
                int i = 0;
                int j = n - 1;
                while (i < neg_count && j >= neg_count) {
                    while (j >= neg_count && arr[i] * (long long)arr[j] < mid) {
                        j--;
                    }
                    count += (n - neg_count) - (j - neg_count + 1);
                    i++;
                    j = n - 1; // Reset j
                }
            }
        }

        return count;
    };

    // Binary search over possible product values
    long long left = min_product;
    long long right = max_product;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        long long total_pairs = (long long)n * (n - 1) / 2;
        long long count = countGE(mid);

        // Number of products greater than or equal to 'mid'
        long long ge_count = total_pairs - count;

        if (ge_count >= k) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return right;
}