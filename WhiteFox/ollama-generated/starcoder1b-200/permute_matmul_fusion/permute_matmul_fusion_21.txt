
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = x1.permute(0, 2, 1)
        t2 = torch.bmm(t1, x2)
        return t2


# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 2, 3)
