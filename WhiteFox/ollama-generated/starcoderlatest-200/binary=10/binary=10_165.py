
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64*3, 128)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 64 * 64 * 3))
        v2 = v1 + other
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.zeros_like(v1) # Replace this by a random value
