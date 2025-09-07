
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, head_dim):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            embed_dim=head_dim, num_heads=4)
 
    def forward(self, qk):
        v1, attn  = self.attn(qk) # Use the same query for all heads (no need to pass in separate queries)
        scaled_attn = attn.mul(scale_factor) # Scale the dot product by a factor 
        softmax_attn = scaled_attn.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_attn = torch.nn.functional.dropout(
            softmax_attn, p=dropout_p)  # Apply dropout to the softmax output
        v2 = dropout_attn.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return v2


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
