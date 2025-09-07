
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.nn.Bmm2d(2, 1)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.bmm.weight, self.bmm.bias)
        return v2


# Inputs to the model
x1  = torch.randn(1, 3, 5, 3)
x2  = torch.randn(1, 4, 2, 2)
