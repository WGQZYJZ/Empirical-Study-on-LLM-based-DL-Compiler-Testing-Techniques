
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1, other=None):
        if other is None:
            v4 = v3 + 0.7071067811865476
        else:
            v4 = v3 + other 
        return torch.relu(v4)
 

# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(2, 32, 64, 64)
 v3 = m(x1) # input tensor of dimension (2, 8)

 