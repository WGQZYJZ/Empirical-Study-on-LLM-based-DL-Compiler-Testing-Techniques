
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1).contiguous()
        v2 = x2.permute(0, 1, 2).contiguous()
        v3 = torch.bmm(v1, v2)
        return torch.nn.functional.linear(v3, self.linear1.weight, self.linear1.bias) +\
               torch.nn.functional.linear(v3, self.linear2.weight, self.linear2.bias)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 3)
