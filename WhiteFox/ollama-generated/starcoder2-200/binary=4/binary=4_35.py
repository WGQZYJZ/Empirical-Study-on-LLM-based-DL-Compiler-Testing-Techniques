
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v1 + other

# Initializing the model
m  = Model()

 # Inputs to the model
other = torch.randn(1, 3)
x = torch.randn(4096, 512)
__output__  = m(x)

