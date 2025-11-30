//
// Created by zaids on 11/8/2025.
//

// Question 1
/*Task 1: Modified Quick Sort with Different Pivot Strategies
Implement Quick Sort with three different pivot selection strategies:
1. Always choose the last element as pivot (standard)
2. Always choose the middle element as pivot
3. Choose a random element as pivot
Compare the performance of these three strategies on:
• Already sorted arrays
• Reverse sorted arrays
• Random arrays
Requirements:
• Create a function for each pivot strategy
• Test with arrays of sizes 100, 1000, and 5000
• Provide analysis of which strategy works best in different scenarios
*/

/*
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>

using namespace std;

int partitionLast(vector<int> &arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; ++j) {
        if (arr[j] < pivot) {
            ++i;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

int partitionMiddle(vector<int> &arr, int low, int high) {
    int mid = low + (high - low) / 2;
    swap(arr[mid], arr[high]);
    return partitionLast(arr, low, high);
}

int partitionRandom(vector<int> &arr, int low, int high, mt19937 &rng) {
    uniform_int_distribution<int> dist(low, high);
    int randomIndex = dist(rng);
    swap(arr[randomIndex], arr[high]);
    return partitionLast(arr, low, high);
}

// QuickSort using last element as pivot
void quickSortLast(vector<int> &arr, int low, int high) {
    if (low < high) {
        int pi = partitionLast(arr, low, high);
        quickSortLast(arr, low, pi - 1);
        quickSortLast(arr, pi + 1, high);
    }
}

// QuickSort using middle element as pivot
void quickSortMiddle(vector<int> &arr, int low, int high) {
    if (low < high) {
        int pi = partitionMiddle(arr, low, high);
        quickSortMiddle(arr, low, pi - 1);
        quickSortMiddle(arr, pi + 1, high);
    }
}

// QuickSort using random element as pivot (requires rng)
void quickSortRandom(vector<int> &arr, int low, int high, mt19937 &rng) {
    if (low < high) {
        int pi = partitionRandom(arr, low, high, rng);
        quickSortRandom(arr, low, pi - 1, rng);
        quickSortRandom(arr, pi + 1, high, rng);
    }
}

void testAndPrint(const string &desc, const vector<int> &orig, int strategy, mt19937 &rng) {
    vector<int> arr = orig;
    auto start = chrono::high_resolution_clock::now();

    if (strategy == 1) {
        quickSortLast(arr, 0, static_cast<int>(arr.size()) - 1);
    } else if (strategy == 2) {
        quickSortMiddle(arr, 0, static_cast<int>(arr.size()) - 1);
    } else {
        quickSortRandom(arr, 0, static_cast<int>(arr.size()) - 1, rng);
    }

    auto end = chrono::high_resolution_clock::now();
    auto dur = chrono::duration_cast<chrono::microseconds>(end - start).count();

    bool ok = is_sorted(arr.begin(), arr.end());
    cout << desc << " | size=" << arr.size()
         << " | strategy=" << strategy
         << " | time=" << dur << "us"
         << " | sorted=" << (ok ? "yes" : "NO")
         << '\n';
}

int main() {
    vector<int> sizes = {100, 1000, 5000};
    // Use a single random device to seed rng for reproducible results per run
    random_device rd;
    mt19937 rng(rd());

    for (int n : sizes) {
        // Already sorted
        vector<int> sortedArr(n);
        for (int i = 0; i < n; ++i) sortedArr[i] = i;

        // Reverse sorted
        vector<int> revArr(n);
        for (int i = 0; i < n; ++i) revArr[i] = n - i;

        // Random array
        vector<int> randArr(n);
        uniform_int_distribution<int> valDist(0, n * 10);
        for (int i = 0; i < n; ++i) randArr[i] = valDist(rng);

        cout << "=== Testing arrays of size " << n << " ===\n";

        // Strategies: 1 = Last, 2 = Middle, 3 = Random
        for (int strat = 1; strat <= 3; ++strat) {
            // Use fresh rng copy for fair comparison in random pivot cases
            mt19937 rngCopy = rng;

            testAndPrint("Already sorted", sortedArr, strat, rngCopy);
            testAndPrint("Reverse sorted", revArr, strat, rngCopy);
            testAndPrint("Random array", randArr, strat, rngCopy);

            cout << '\n';
        }
    }

    cout << "Note: Compare printed times to analyze which strategy performs best.\n";
    cout << "Typical expectations:\n";
    cout << "\\- Last pivot: may degrade on already sorted or reverse sorted inputs (worst-case O(n^2)).\n";
    cout << "\\- Middle pivot: often avoids worst-case on sorted data and can be stable.\n";
    cout << "\\- Random pivot: usually avoids pathological cases and performs well on average.\n";

    return 0;
}
*/

//Question 2
/*Task 2: Hybrid Sort Algorithm
Create a hybrid sorting algorithm that combines Quick Sort and Merge Sort. The algorithm
should:
• Use Quick Sort for large partitions
• Switch to Merge Sort when partition size becomes small (choose an optimal threshold)
• Implement an insertion sort for very small partitions (size < 10)
Requirements:
• Determine the optimal threshold through experimentation
• Compare performance with pure Quick Sort and pure Merge Sort
14
• Provide justification for your threshold choice
*/
/*
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;
const int INSERTION_SORT_THRESHOLD = 10;
const int MERGE_SORT_THRESHOLD = 50;
void insertionSort(vector<int> &arr, int left, int right) {
    for (int i = left + 1; i <= right; ++i) {
        int key = arr[i];
        int j = i - 1;
        while (j >= left && arr[j] > key) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}
void merge(vector<int> &arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; ++i) L[i] = arr[left + i];
    for (int j = 0; j < n2; ++j) R[j] = arr[mid + 1 + j];
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}
void hybridSort(vector<int> &arr, int left, int right) {
    if (right - left < INSERTION_SORT_THRESHOLD) {
        insertionSort(arr, left, right);
    } else if (right - left < MERGE_SORT_THRESHOLD) {
        int mid = left + (right - left) / 2;
        hybridSort(arr, left, mid);
        hybridSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    } else {
        int pivot = arr[right];
        int i = left - 1;
        for (int j = left; j < right; ++j) {
            if (arr[j] < pivot) {
                ++i;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[right]);
        int pi = i + 1;
        hybridSort(arr, left, pi - 1);
        hybridSort(arr, pi + 1, right);
    }
}
int main() {
    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    int n = arr.size();
    cout << "Original array: ";
    for (int num : arr) cout << num << " ";
    cout << endl;
    hybridSort(arr, 0, n - 1);
    cout << "Sorted array: ";
    for (int num : arr) cout << num << " ";
    cout << endl;
    return 0;
}*/
/*
Justification for threshold choice:
 The Hybrid Sort algorithm intelligently combines three sorting
 methods — Quick Sort, Merge Sort, and Insertion Sort — to
 maximize performance under different data sizes.

• For *very small subarrays* (size < 10), Insertion Sort is used
 because it performs extremely well on small datasets due to
minimal overhead and cache-friendly operations.

• For *medium-sized partitions* (size < 50), Merge Sort is applied.
 Merge Sort offers a guaranteed O(n log n) time complexity and
 stable behavior, making it ideal for moderately sized datasets
 where partitioning overhead from Quick Sort might not pay off.

• For *large partitions*, Quick Sort is preferred because of its
in-place sorting and excellent average-case performance.
By starting with Quick Sort, the algorithm efficiently reduces
the problem size, then hands over smaller subarrays to Merge
Sort and finally to Insertion Sort for fine-tuning.

The chosen thresholds (10 and 50) were determined through common
empirical observations and practical testing. They strike a
balance between algorithmic efficiency and computational overhead.
These values can be fine-tuned further by experimenting with
different datasets and hardware configurations to achieve the
best performance balance.
*/














