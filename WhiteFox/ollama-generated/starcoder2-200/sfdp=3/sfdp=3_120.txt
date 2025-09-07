
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key) # Compute the dot product of the query and key tensors 
        v2  = v1 * 0.5
        v3  = torch.erf(v2)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(8, 8, 4) # Initialize the query tensor
key    = torch.randn(16, 7, 4) # Initialize the key tensor
value  = torch.randn(32, 5, 9) # Initialize the value tensor

