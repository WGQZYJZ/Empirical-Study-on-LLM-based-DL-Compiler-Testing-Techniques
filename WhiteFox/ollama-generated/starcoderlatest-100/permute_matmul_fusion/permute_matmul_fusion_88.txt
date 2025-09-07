
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.bmm(x1.permute(0, 2, 1), x2)  # or torch.matmul(x1.permute(0, 2, 1), x2)
        v2 = self.matmul(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 2, 3, 4)
x2 = torch.randn(1, 5, 7, 8)
