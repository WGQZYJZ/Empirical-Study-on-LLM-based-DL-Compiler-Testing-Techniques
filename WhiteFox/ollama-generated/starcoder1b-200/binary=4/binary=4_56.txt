
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) + other
        return v1


# Inputs to the model
input_tensor = torch.randn(1, 32, 64, 64)
