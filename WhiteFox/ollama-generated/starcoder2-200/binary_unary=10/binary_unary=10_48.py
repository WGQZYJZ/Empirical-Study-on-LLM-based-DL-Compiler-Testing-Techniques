
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(784, 50)
        self.lin2 = torch.nn.Linear(50, 10)
 
    def forward(self, x1):
        v1 = self.lin1(x1)
        v2 = v1 + other # Replace the constant 9 with another tensor or a parameter
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(784, 640)
