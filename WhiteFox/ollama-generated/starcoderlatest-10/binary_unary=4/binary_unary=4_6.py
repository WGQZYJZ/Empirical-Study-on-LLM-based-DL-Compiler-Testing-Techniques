
class Model(torch.nn.Module):
    def __init__(self, other_tensor: torch.Tensor=None):
        super().__init__()
        self.conv = torch.nn.Linear(128, 16)
        self.other = other_tensor
 
    def forward(self, x1):
        v1 = self.conv(x1) + self.other
        v2 = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
