class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> temp;
        int k = 0;
        int j = 0;
        while(k < m && j < n)
        {
            if(nums1[k] < nums2[j])
            {
                temp.push_back(nums1[k]);
                k++;
            }
            else
            {
                temp.push_back(nums2[j]);
                j++;
            }
        }
        while(k < m)
        {
            temp.push_back(nums1[k]);
            k++;
        }
        while(j < n)
        {
            temp.push_back(nums2[j]);
            j++;
        }
        nums1 = std::move(temp);
    }
};