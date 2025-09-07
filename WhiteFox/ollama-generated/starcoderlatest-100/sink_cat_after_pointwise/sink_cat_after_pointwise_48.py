
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1, x1, x1], dim=1)
        t2 = t1.view(-1, 9)
        t3 = torch.relu(t2)
        return t3


# Inputs to the model
x1 = torch.randn(10, 64, 64)
