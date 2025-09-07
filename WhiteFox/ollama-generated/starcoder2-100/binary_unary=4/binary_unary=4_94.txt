
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32,10)
 
    def forward(self, x1, other):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = torch.relu(v2) # Applying ReLU activation function to the result of the previous transformation
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1, x2  = torch.randn(4, 32), torch.rand(4, 10)
__output__  = m(x1, other=x2)

