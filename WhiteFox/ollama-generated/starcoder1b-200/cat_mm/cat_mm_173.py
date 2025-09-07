
class Model(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        return x1 @ x2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(2, 5)
