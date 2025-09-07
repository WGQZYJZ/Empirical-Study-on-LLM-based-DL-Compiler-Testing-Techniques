
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 16 * 16, 64)
        self.other = other
 
    def forward(self, x1):
        v1 = F.relu(self.linear(x1))
        v2 = self.other + v1
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 32, 64, 64)
