
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v0 = self.linear(x1) # Apply linear transformation to the input tensor
        v2 = (v0 + 3).clamp_min(0).clamp_max(6) / 6
        return v2

# Initializing model
m = Model()

