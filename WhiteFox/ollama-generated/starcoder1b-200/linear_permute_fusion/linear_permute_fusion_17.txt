
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = self.linear(x1)
        return v.permute(0, 2, 1)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 2)
