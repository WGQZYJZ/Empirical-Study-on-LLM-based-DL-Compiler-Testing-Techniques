
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Linear transformation to the input tensor
        v2 = v1 - other_tensor
        return v2


# Initializing the model
m = Model()

# Inputs to the model
other_tensor  = torch.randn(8,3)
x1  = torch.randn(50, 3) # Input tensor of size (50, 3) with elements randomly sampled from a normal distribution
__output__  = m(x1).sum()

