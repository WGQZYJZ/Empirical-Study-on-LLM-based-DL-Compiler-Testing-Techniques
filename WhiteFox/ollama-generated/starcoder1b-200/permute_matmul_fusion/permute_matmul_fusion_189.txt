
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        t1 = x1.permute(0, 2, 1)
        t3 = torch.bmm(t1, self.linear.weight)  # or torch.matmul(t1, self.linear.weight)
        return t3


# Inputs to the model
x1 = torch.randn(2, 2, 2)
x2 = torch.randn(2, 2, 2)
