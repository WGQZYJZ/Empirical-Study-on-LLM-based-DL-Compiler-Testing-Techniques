
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 8)
 
    def forward(self, x1, other):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = F.relu(v2) 
        return v3

# Initializing the model
m  = Model()
other_tensor  = torch.randn(8,) # You can choose a different constant tensor of shape (8, ) or use random.random(size=(10,))


# Inputs to the model
x1   = torch.randn(16, 32)
