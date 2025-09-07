
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - other_const
        v3 = F.relu(v2)
        return v3


# Initializing the model
m2 = Model2()

 # Inputs to the model
x  = torch.randn(64, 784)
__output2__ = m2(x)

