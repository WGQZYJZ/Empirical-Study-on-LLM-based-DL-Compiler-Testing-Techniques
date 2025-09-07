
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other # <---- This is the new part 
        return v2
 
# Initializing the model and specifying "other" as a constant tensor
m   = Model()
other  = torch.randn(3, 16)
 
# Inputs to the model
x   = torch.randn(1000, 32)
__output__  = m(x)

