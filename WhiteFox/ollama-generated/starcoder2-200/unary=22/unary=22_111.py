
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x = torch.randn(30)


# Initializing the model with a custom weight
w = torch.ones(5, 10)/4


# Initializing the model with a custom bias
b = torch.zeros(5,) + 3


m(x).shape == torch.Size([30])

