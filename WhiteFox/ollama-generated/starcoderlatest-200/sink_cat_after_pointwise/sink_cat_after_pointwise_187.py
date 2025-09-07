
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        v = torch.relu(t1)
        u = torch.cat([v, t2], dim=0)
        return u

# Inputs to the model
x1 = torch.randn(1, 2, 2)
