
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        t1 = x.permute(0, 2, 1)
        return self.linear(t1)


# Inputs to the model
x  = torch.randn(1, 3, 1)
