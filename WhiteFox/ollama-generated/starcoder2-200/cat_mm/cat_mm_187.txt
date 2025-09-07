
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.mm(x1, self) + 1 # Apply matrix multiplication and add 1 to the result of the multiplication operation

        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(32)
x2 = torch.randn(32, 32)

