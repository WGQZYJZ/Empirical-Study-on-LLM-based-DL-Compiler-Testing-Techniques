
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32 * 16, 8)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = relu(v1) # Activation function
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(30, 32 * 16)
__output__  = m(x1)

