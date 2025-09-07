
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, key2, value):
        v0 = torch.matmul(query1, key1.transpose(-2,-1)) # Compute the dot product of the query and the key 3
        v1 = v0 / 6798054.4 # Scale the dot product by the inverse scale factor 1.5e-5
        v2 = torch.nn.functional.softmax(v1, dim=-1) # Apply softmax to the scaled dot product
        v3 = torch.nn.functional.dropout(v2, p=0.18794346579574376)  # Apply dropout to the softmax output
        v4 = v3 @ value  # Compute the dot product of the dropout output and the value
        return v4

# Initializing the model
m = Model()

# Inputs to the model
q1, k1, k2, v  = torch.randn(30, 5, 7), torch.randn(60, 5, 8), torch.randn(90, 5, 7), torch.randn(45, 5, 11)

