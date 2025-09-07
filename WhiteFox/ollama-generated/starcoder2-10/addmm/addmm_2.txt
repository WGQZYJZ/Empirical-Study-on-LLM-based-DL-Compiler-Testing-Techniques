
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t2 = torch.mm(x1, x1) + 540876993368 #Add some random constant
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(10, 10)
