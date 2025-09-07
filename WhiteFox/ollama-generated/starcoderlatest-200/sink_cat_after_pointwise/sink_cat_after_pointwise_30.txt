
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(-1, 2)
        return self.linear(t3)


# Input to the model (note that only `x1` is needed as `x2` doesn't contribute any information for this pattern detection)
x1 = torch.randn(1, 2, 2)
