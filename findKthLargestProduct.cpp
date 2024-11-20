//Write a C++ function findKthLargestProduct that finds the k-th largest unique product of two distinct elements in an integer array arr. 
//The function must: Run in O(n log n) time complexity.

#include <iostream>
#include <vector>
#include <algorithm>

long long findKthLargestProduct(std::vector<int>& arr, int k) {
    if (arr.size() < 2 || k <= 0 || k > (arr.size() * (arr.size() - 1)) / 2) {
        return -1; // Invalid input
    }

    std::vector<long long> products;
    for (size_t i = 0; i < arr.size(); ++i) {
        for (size_t j = i + 1; j < arr.size(); ++j) {
            products.push_back((long long)arr[i] * (long long)arr[j]);
        }
    }

    std::sort(products.begin(), products.end(), std::greater<long long>());

    // Remove duplicates (this can be optimized further for space efficiency)
    products.erase(std::unique(products.begin(), products.end()), products.end());

    if (k > products.size()) {
        return -1; // k is out of bounds after removing duplicates
    }

    return products[k - 1];
}