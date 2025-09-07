
class SelfAttentionLayer(torch.nn.Module):
    def __init__(self, num_attn_heads, dropout_p):
        super().__init__()

        self.num_attn_heads = num_attn_heads
        self.dropout_p = dropout_p
 
        # The input tensor should have shape (batch_size, seq_length, dim)
        # with the `seq_length` as the length of each sequence in the batch. 
        # The output tensor will be same as that of the input tensor

        ...

    def forward(self, x):
        attn_mask = torch.ones_like(x).float()
        ...
 
        # The size of the attention weights is `seq_length` and `num_attn_heads`.
        
        v  = ... 

        return output


# Initializing the model
m = SelfAttentionLayer(2, dropout_p=0.1) 

# Inputs to the model
x = torch.randn(4, 32, 768)
