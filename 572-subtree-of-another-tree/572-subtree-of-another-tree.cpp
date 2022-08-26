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
public:
    bool isSameTree(TreeNode* root, TreeNode* subRoot) {
        if(root == nullptr || subRoot == nullptr)
            return (root == subRoot);                 // if both are null then only return true.
        
        if(root->val != subRoot->val) return false;
        bool isLeftSubtreeSame = isSameTree(root->left, subRoot->left);
        bool isRightSubtreeSame = isSameTree(root->right, subRoot->right);
        
        return (isLeftSubtreeSame &&  isRightSubtreeSame);
    }
    
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(subRoot == nullptr) return true;
        if(root == nullptr) return false;
        
        if(isSameTree(root, subRoot)) return true;
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};