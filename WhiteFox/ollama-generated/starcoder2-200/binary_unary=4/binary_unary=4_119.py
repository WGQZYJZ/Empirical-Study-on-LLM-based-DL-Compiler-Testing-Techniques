
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(64, 784)

# Keyword argument for the forward method (other): A tensor that is added to the output of a linear transformation

__output__  = m(x1, other=torch.ones([64, 5]))

