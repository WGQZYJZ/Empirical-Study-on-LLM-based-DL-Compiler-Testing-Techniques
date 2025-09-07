
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        return torch.bmm(v1, self.linear.weight), torch.matmul(v1, self.linear.weight)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
y2 = torch.randn(1, 2, 2)
