
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 4)

    def forward(self, x1):
        return x1 + self.linear(x1).permute(0, 2, 1)

# Inputs to the model
x1 = torch.randn(1, 1, 4)
