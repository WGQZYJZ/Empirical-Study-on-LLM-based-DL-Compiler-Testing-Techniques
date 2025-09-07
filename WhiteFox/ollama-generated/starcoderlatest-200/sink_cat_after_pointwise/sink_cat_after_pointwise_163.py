
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        t1 = torch.cat([x1, x2], dim=0)
        v2 = t1.view(-1, 4)
        t3 = torch.relu(v2)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
x2 = torch.randn(1, 4)
x3 = torch.randn(1, 2)
