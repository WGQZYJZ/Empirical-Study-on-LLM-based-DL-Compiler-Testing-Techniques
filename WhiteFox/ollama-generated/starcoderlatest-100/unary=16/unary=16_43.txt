
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 8, 16)
 
    def forward(self, x1):
        v1 = x1.view(-1, 32 * 32 * 8)
        v2 = self.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
