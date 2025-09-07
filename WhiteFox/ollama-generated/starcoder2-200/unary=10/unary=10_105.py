
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x):
        y = self.linear(x)
        return (y + 3).clamp(min=0, max=6) / 6


# Initializing the model
model = Model()
 
# Inputs to the model
input_tensor = torch.randn(128, 28 * 28)
