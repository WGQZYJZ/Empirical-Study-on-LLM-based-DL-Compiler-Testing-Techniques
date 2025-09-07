
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).type(torch.float) * -1  # Use the negative slope instead of the default value, i.e., "0"
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
