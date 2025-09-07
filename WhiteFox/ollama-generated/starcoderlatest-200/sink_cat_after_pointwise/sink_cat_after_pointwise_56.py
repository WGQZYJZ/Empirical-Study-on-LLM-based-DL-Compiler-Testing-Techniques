
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, ...):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(-1, 8)
        t3 = torch.relu(t2)
        return t3

# Inputs to the model
x1 = torch.randn(5, 2, 2)
x2 = torch.randn(3, 2, 2)
