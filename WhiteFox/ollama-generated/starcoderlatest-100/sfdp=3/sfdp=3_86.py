
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads):
        super().__init__()
        self.num_heads = num_heads
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
m = MultiHeadAttention(2)

# Inputs to the model
query  = torch.randn(1, 256, 7, 7)
key    = torch.randn(1, 256, 13, 13)
value  = torch.randn(1, 256, 8, 8)
scale_factor = torch.eye(3).unsqueeze(0)
dropout_p = 0.5
