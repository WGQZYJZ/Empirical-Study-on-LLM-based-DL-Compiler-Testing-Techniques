
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(64 * 10 * 10, 32)
 
    def forward(self, x1):
        v1 = x1.view(-1, 64 * 10 * 10)
        v2 = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
