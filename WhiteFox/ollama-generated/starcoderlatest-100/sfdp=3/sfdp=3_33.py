
class Attention(torch.nn.Module):
    def __init__(self, num_heads, dim):
        super().__init__()
        self.num_heads = num_heads
        self.linear = torch.nn.Linear(dim, num_heads * 3)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Attention(1024, 16)
 
# Inputs to the model
query = torch.randn(32, 32, 1024, device=device)
key = torch.randn(32, 32, 1024, device=device)
value = torch.randn(32, 32, 16 * 1024, device=device)
