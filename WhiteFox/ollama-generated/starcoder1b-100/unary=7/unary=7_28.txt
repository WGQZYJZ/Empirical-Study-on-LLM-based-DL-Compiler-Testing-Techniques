
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(min=0, max=6, l1 + 3)  # Apply clamping to the linear transformation's output
        v3 = v2 / 6
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
