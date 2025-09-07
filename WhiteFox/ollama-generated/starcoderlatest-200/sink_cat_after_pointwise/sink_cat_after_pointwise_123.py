
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(-1, 4)
        t3 = torch.relu(t2)
        return t3


# Inputs to the model
x1 = torch.randn(2, 2, requires_grad=True)
x2 = torch.randn(2, 2, requires_grad=True)
