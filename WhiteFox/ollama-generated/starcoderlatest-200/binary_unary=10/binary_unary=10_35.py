
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 128)
 
    def forward(self, x1, x2):
        v1 = self.linear(x1.view(-1, -1))
        v2 = v1 + x2.view(-1)
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(800, 3 * 64 * 64)
x2 = torch.randn(800)
