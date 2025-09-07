
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16 * 8 * 8, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.shape[0], -1))
        return torch.relu(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 16 * 8 * 8)
