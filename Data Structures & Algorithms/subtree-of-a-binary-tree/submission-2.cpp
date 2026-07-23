/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    bool isSameTree(TreeNode *n1, TreeNode *n2) {
        if (n1 == nullptr && n2 == nullptr) return true;
        if (n1 == nullptr || n2 == nullptr) return false;
        if (n1 -> val != n2 -> val) return false;
        return isSameTree(n1->left, n2->left) && isSameTree(n1->right, n2->right);    
    }
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (root == nullptr && subRoot == nullptr) return true;
        if (root == nullptr) return false;
        if (subRoot == nullptr) return false;

        if (root->val == subRoot->val) {
            bool same = isSameTree(root, subRoot);
            if (same) return true;
        }
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};
