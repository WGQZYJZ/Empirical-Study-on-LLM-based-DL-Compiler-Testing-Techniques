
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784,10)
 
    def forward(self, x):
        v2 = F.relu(self.linear(x))
        return v2


# Initializing the model
m  = Model()
# Inputs to the model
x = torch.randn(64, 784)
__output__  = m(x)


