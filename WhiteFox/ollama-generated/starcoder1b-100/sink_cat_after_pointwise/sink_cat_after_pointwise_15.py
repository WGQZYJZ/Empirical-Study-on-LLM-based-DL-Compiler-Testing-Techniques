
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2, x3], dim=-1)
        return torch.relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
input1  = torch.randn(1, 4, 4)
input2  = torch.randn(1, 4, 3)
input3  = torch.randn(1, 5, 6)
