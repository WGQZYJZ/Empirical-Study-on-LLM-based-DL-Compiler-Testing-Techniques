
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = F.relu(v1) # Here, we use a common PyTorch function, which is F.relu(v1). 
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(64, 784)
__output__  = m(x)

