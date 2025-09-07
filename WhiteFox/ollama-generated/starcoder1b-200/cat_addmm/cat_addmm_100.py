
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32, 10)
 
    def forward(self, x):
        x = x + 0.5  # Add 0.5 to the input
        x = x * 2.0  # Multiply the input by 2.0
        x = torch.addmm(x, self.fc.weight, self.fc.bias)
        return x


# Initializing the model
m = Model()

