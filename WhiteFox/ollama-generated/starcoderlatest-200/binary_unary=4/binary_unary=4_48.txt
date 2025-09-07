
class Model(torch.nn.Module):
    def __init__(self, other=torch.tensor([1., 2., 3.], dtype=torch.float)):
        super().__init__()
        self.conv = torch.nn.Linear(64 * 64 * 3, 8)
 
    def forward(self, x1):
        v1 = self.conv(x1.reshape(-1, 3 * 64 * 64))
        v2 = v1 + other
        v3 = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
