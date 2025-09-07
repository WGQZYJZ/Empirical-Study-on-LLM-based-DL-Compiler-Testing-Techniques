
class MultiHeadSelfAttention(nn.Module):
    def __init__(self,
                 dim_model, 
                 num_heads=16,
                 dropout_p=0.5):
        super().__init__()
 
        self.dropout = nn.Dropout(dropout_p)
 
        self.num_heads = num_heads  # Number of heads to split the input tensor into
        
        # Compute the dimension of the attention projection matrix
        dim_head = int(dim_model/self.num_heads)

        # Linear layers for splitting and combining the heads (a matrix where the number of rows is the same as the number of columns, and all elements are equal to the number of heads)
        self.qkv = nn.Linear(dim_model, dim_head*3, bias=False)

        # Apply a linear transformation to combine multiple attention heads into a single tensor
        self.out = nn.Linear(dim_head * num_heads, dim_model, bias=False)
 
    def split_heads(self, x):
        