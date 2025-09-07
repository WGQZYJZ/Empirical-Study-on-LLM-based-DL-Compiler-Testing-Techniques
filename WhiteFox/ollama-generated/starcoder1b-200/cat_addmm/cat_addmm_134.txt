
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32, 8)
        self.fc2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.fc1(x1) * 0.5
        v2 = self.fc2(v1)
        return v2


# Inputs to the model
x1  = torch.randn(32, 3)
y1  = m(x1)  # Forward pass of the model
__output__  = m.fc2(m.fc1(x1)) * 0.5  # Backward pass of the model


