
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the input and the key
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(3, 8, 64, 64)
