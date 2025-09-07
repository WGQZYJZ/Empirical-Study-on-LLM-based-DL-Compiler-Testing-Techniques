
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 32)
 
    def forward(self, x1):
        v4 = torch.nn.functional.relu(self.linear(x1))
        return v4


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(8)
 
__output__  = m(x1)