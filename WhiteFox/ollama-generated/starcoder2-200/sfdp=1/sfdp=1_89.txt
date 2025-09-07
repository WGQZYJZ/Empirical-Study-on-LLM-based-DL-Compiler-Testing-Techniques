
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v2  = v1 / 4950378767.2656
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=0.1) # Apply dropout to the softmax output
        __output__  = v4.matmul(value) # Compute the dot product of the dropout output and the value tensor


# Initializing the model
m  = Model()

# Inputs to the model
qk  = torch.randn(256, 1024).repeat(32, 1, 1) * 879406967 # Generate a random tensor with 32 repeats of 1024 rows and 2 columns
key  = torch.randn(256, 1024).repeat(32, 1, 1) * 10180348 # Generate a random tensor with 32 repeats of 1024 rows and 2 columns
value  = torch.randn(256, 196608).repeat(32, 1, 1) / 744431785.24 # Generate a random tensor with 32 repeats of 196608 rows and 1 column

