
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 200315)
        self.other = -1
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - self.other # Subtracting -1 is allowed
        v3 = F.relu(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model
m  = Model()
 
# Inputs for the model
x1  = torch.randn(4, 4096)
__output__  = m(x1)

