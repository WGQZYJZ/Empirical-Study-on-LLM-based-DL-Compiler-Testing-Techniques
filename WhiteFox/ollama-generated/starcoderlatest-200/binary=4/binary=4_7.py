
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        return v2


# Inputs to the model
x1 = torch.randn(1, 128, 64, 64)
other_tensor = torch.randn(3, 1)
