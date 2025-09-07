
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64*64*3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other 
        return torch.relu(v2)


# Initializing the model
m  = Model()
 
other  = torch.randn(10) # Random input tensor of shape (1,8). The actual size and value may be different.

# Inputs to the model
x1  = torch.randn(500, 3, 64, 64)
__output__  = m(x1)

