
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 128, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 0.5
        return v1


# Inputs to the model
x1 = torch.randn(1, 64 * 128)
