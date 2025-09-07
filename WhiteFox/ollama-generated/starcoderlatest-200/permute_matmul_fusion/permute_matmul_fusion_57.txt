
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.transpose(x1, 0, 1)
        v2 = torch.transpose(x2, 0, 1)
        v3 = torch.bmm(v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 4)
x2 = torch.randn(1, 5, 5)
