
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 0) + other
        return v1


# Initializing the model
m = Model()


# Inputs to the model
other  = torch.randn(28*28,)
x1  = torch.rand(256, 784,)
 
