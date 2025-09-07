
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = torch.bmm(x1.permute(0, 2, 1), x2.permute(0, 2, 1)) # or torch.matmul(x1, x2)
        v2 = self.linear(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
