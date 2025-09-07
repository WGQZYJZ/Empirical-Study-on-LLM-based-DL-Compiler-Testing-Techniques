
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 4)
 
    def forward(self, x1):
        v2 = self.linear(x1) 
        v3 = torch.clamp_min(v2, -15) 
        v4 = torch.clamp_max(v3, 8.7654321) 
        return v4

# Initializing the model with keyword arguments.
m  = Model(-10.999999999999999, 10.75)

 # Inputs to the model