
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 6)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + 3 
        v3 = torch.clamp_min(v2, 0) # Clamps the values of v2 to a minimum value of 0 by using clamp_min function.
        v4 = torch.clamp_max(v3, 6) # Clamps the values of v4 to a maximum value of 6.
        v5 = v4 / 6 
        return v5

# Initializing the model