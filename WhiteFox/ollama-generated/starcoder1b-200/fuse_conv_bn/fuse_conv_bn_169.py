
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(2, 2)

    def forward(self, x1):
        return self.linear(torch.matmul(x1, self.linear.weight))


# Inputs to the model
x1 = torch.randn(1, 2, 2)
