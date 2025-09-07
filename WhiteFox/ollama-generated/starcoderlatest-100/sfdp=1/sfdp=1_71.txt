
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, n_head, d_k):
        super().__init__()
        self.n_head = n_head # The number of heads in the attention mechanism
        self.d_k  = d_k  # The dimension of each head in the attention mechanism
 
    def forward(self, query, key, value):
        q = torch.matmul(query, k) # Compute the dot product between the query and keys 
        scaled_q = q.div(inv_scale_factor) # Scale the output by the inverse scale factor
        softmax_q = scaled_q.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_q = torch.nn.functional.dropout(softmax_q, p=dropout_p) # Dropout and compute attention scores
 
        attn  = torch.matmul(dropout_q, v) # Apply the attention matrix to the value tensor
        attn = self.layer_norm1(attn + q) # Add query and computed attention scores to the layer norm output of this model
        scaled_attn = attn.div(inv_scale_factor) # Scale by the inverse scale factor for renormalization
        attn  = scaled_attn.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_attn = torch.nn.functional.dropout(attn, p=dropout_p) # Dropout and compute attention scores
 
        output = self.layer_norm2(attn @ v + query) # Add the attention matrix and the renormalization output of this model to the previous layer norm output
        return output

# Inputs to the model
mha  = MultiHeadAttention(8, 32)
q    = torch.randn(4, 32, 64, 64) # Input tensor
k    = torch.randn(32, 64, 16, 16) # Key tensor
v    = torch.randn(32, 64, 16, 16) # Value tensor
