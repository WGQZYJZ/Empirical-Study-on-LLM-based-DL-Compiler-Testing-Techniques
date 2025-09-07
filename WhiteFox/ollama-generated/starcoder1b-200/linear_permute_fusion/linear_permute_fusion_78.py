
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)

    def forward(self, x1):
        v1 = x1.view(1, -1)
        v2 = self.linear(v1).permute(1, 0)
        return v2

# Inputs to the model
x1 = torch.randn(1, 10)
