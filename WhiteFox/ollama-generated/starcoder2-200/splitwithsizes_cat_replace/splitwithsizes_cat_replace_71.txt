
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.split(x1, 32000, dim=0) + 1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(784*5)


# Outputs of the model
output = m(x1)

