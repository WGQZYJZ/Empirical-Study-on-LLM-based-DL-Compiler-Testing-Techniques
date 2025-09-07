
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 16)
    
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = torch.clamp_min(v1, -10) # Clamp the output of the linear transformation to -10
        v3  = torch.clamp_max(v2, 15) # Clamp the output of the previous operation to 15
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(4096, 3)
__output__  = m(x1)

