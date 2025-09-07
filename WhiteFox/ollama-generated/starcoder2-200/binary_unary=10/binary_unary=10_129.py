
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 32, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1))
        v2  = v1 + other_tensor
        v3  = torch.relu(v2) # This line is added 
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3*32 * 32)

# Output tensor from the model
__output__  = m(x1)

