
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 64 * 64, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + torch.randn(v1.size()) # Please provide a non-negative tensor


# Initializing the model
m = Model()

# Inputs to the model
x2  = torch.randn(3, 32, 64, 64)
__output__  = m(x2) 
