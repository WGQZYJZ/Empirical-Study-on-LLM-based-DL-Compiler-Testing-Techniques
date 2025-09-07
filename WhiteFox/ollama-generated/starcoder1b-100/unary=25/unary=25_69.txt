
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = v1 * -1
        v3 = v1 * 0.75
        return v4


# Inputs to the model
x1 = torch.randn(1, 10)
