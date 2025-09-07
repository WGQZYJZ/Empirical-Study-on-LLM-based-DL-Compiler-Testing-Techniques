
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm1 = torch.nn.BMM(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.bmm1.weight_a, self.bmm1.bias_a)
        v3 = x2.permute(0, 2, 1)
        return torch.bmm(v2, v3)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
