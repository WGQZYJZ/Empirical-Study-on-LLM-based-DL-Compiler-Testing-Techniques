
class Model(torch.nn.Module):
    def __init__(self, other=10.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (x1 - other)
        return v2


# Inputs to the model
input_tensor = torch.randn(3, 5)
