
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v1 + other
 
# Initializing the model with a random value for 'other'
m = Model()
other = torch.randn(1024)

 # Inputs to the model:
x = torch.randn(3, 1024)
__output__  = m(x)
