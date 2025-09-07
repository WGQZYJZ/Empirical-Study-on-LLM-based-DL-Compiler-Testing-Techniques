

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 45.0 # Replace the value of 45.0 with a real tensor 
        return v1


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 32)
__output__  = m(x1)

# Initializing the model