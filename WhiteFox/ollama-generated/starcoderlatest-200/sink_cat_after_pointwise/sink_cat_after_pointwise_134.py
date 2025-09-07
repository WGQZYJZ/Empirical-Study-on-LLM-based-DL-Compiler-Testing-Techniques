
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        v1 = t1.view(-1)
        t2 = torch.relu(v1)
        return t2


# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(3, 5)
