
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(512*7*7, 4096)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + torch.randn_like(v1) # Use a tensor generated with random values instead of a constant value
        v3  = F.relu(v2)
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 512*7*7)
