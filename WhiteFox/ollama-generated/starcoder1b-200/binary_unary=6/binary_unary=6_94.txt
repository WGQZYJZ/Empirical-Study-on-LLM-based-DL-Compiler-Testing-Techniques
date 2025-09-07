
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) - 3.9324325325325 # Subtract '3.9324325325325' from the output of the linear transformation
        return torch.relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 8, 64, 64)
