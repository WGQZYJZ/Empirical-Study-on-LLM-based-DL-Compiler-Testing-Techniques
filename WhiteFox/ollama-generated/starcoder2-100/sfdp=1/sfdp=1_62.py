
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.matmul(x1, x2)
        v1 = torch.tanh(v0)  # Apply the tanh function to each value in the tensor
        v3 = torch.matmul(v1, torch.transpose(v1, -2, -1))
        return v4


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(3)
x2 = x1 # Initialize with the same value as previous input tensor
 
__output__  = m(x1, x2)