
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        if other_tensor is not None:
            self.linear = torch.nn.Linear(1024, 512)
        else:
            self.other_tensor = other_tensor
 
    def forward(self, x1):
        v1 = self.linear(x1) + (0.0 if self.other_tensor is None else self.other_tensor)
        v2 = torch.nn.functional.relu(v1)
        return v2
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
