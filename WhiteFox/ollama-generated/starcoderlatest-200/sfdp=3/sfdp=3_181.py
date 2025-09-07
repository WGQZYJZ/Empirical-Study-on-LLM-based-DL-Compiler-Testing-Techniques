
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads, head_dim):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = head_dim
 
    def forward(self, query, key, value, scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.9)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = MultiHeadAttention(2, 16)

# Inputs to the model
query = torch.randn(1, 8, 20, 256)  # [batch_size=1, num_heads=8, q_len=20, d_k=256]
key = torch.randn(1, 8, 10, 256)   # [batch_size=1, num_heads=8, k_len=10, d_k=256]
value = torch.randn(1, 8, 20, 256) # [batch_size=1, num_heads=8, v_len=20, d_k=256]
