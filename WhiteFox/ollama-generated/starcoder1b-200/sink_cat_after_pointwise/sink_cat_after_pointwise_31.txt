
class Model(torch.nn.Module):
    def __init__(self, n_hidden=50, dropout=0):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat([x2.permute(0, 2, 1), self.linear.weight, self.linear.bias], dim=1)
        return tanh(self.linear(v3))


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
