
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return self.__linear__(x1).permute(0, 2, 1) # Permute the output from the linear transformation


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
