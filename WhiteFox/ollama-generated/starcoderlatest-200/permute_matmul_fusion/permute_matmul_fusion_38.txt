
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = torch.nn.Linear(2, 2)
        self.linear_2 = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1  = x1.permute(0, 2, 1)
        v2  = torch.nn.functional.linear(v1, self.linear_1.weight, self.linear_1.bias)
        v3  = x2.permute(0, 2, 1)
        v4  = torch.nn.functional.linear(v3, self.linear_2.weight, self.linear_2.bias)
        return torch.bmm(v2, v4)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
