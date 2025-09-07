
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.forward_v0(x1)
        return self.forward_v1(v1)

    def forward_v0(self, x2):
        v2 = torch.nn.functional.linear(x2, 0, 1)
        return v2

    def forward_v1(self, v2):
        v3 = self.forward_v2(v2)
        return v3

# Inputs to the model
x1 = torch.randn(1, 2, 2)
