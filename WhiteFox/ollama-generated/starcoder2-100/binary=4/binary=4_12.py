
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 8)
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2 = v1 + torch.randn(v1.size()) # Add another random tensor to the output of the linear transformation
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3, 64, 64)
__output__  = m(x1)

