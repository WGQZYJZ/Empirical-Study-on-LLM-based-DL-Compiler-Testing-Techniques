
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return torch.bmm(x1.permute(0, 2, 1), self.linear.weight).permute(0, 2, 1)


# Inputs to the model
t1 = torch.randn(2, 3, 4)
t2 = torch.randn(2, 5, 6)
