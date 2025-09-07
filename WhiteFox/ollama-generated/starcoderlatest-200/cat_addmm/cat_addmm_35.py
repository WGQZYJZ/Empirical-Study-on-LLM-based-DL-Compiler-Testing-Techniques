
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = v1  # No change
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
