
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk * scale_factor # Scale the dot product by a factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)  # Apply dropout to the softmax output
        return dropout_qk * value # Compute the dot product of the dropout output and the value tensor


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(8, 32, 64, 64) # Shape: (batch size, num_heads, query length, key length)
key = torch.randn(8, 32, 64, 64)
scale_factor = 0.5
