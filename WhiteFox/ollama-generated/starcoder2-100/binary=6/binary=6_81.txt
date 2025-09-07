
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        return v1 - other
 
# Initializing the model
m2 = Model2()

 # Inputs to the model
x  = torch.randn(16, 784)
__output__  = m2(x)

