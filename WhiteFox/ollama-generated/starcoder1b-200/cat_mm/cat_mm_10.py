
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        return torch.cat([x1, x1, x2, x2])


# Inputs to the model
input1 = torch.randn(3, 4, 5)
input2 = torch.randn(3, 4, 6)
