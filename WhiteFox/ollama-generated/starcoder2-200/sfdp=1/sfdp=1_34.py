
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v3  = v1 / inv_scale_factor # Scale the dot product by the inverse scale factor
        v4  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        v6  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor 
        return v6


# Initializing the model
m = Model()

# Inputs to the model
__query__ = torch.randn(10, 32, 8, 7)
key = torch.randn(10, 32, 4, 5)
value = torch.randn(10, 32, 16, 9)

