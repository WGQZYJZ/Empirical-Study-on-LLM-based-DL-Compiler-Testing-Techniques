
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
        v3 = F.relu(v2)
        return v3


m = Model()
 
 # Inputs to the model
x = torch.randn(5, 784)
 
other = torch.randn_like(input=x)
 
__output__  = m(x)

# Initializing the model
m  = Model()
 
 
# Inputs to the model
x1 = torch.randn(32, 1, 64, 64)


