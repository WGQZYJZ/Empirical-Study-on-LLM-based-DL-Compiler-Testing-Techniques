
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(10, 2)
 
    def forward(self, x):
        v1 = self.lin(x)
        v3 = relu(v1 + other)

# Initializing the model