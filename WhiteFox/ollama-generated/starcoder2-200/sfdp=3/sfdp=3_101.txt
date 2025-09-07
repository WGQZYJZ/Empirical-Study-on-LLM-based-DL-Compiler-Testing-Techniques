
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v3  = v1.mul(scale_factor) # Scale the dot product by a factor
        v4  = v3.softmax(dim=-1) # Apply softmax to the scaled dot product
        v5  = torch.nn.functional.dropout(v4, p=dropout_p) 
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(20, 32, 64, 64)
x2  = torch.randn(20, 80, 64, 64)
__output__  = m(x1, x2)

