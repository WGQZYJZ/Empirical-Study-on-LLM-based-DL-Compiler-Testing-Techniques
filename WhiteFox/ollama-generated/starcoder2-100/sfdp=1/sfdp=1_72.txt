

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        v2 = v1 / math.sqrt(scale_factor)   # Scale the dot product by the sqrt of scale factor
        v3 = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)  # Apply dropout to the softmax output
        v5 = v4.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return v5

# Initializing the model
m = Model()

# Inputs to the model
query1, key1, value1  = torch.randn(32, 64), torch.randn(32, 64, 64), torch.randn(32, 64, 64)

