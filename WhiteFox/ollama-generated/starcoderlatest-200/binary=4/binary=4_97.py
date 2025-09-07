
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 512)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1.view(-1, 64 * 64 * 3))
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
