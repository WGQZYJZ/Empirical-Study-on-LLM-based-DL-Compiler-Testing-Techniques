
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        return v2


# Initializing the model
m = Model()
 
other_tensor  = torch.randn(len(x1), len(y))  # Some arbitrary tensor

# Inputs to the model
x1, y  =  torch.randn(10, 32)
__output__  = m(x1)

