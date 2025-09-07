
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = torch.clamp_min(v1, -50) # Apply the clamp function with a minimum value of -50 to the output of the linear transformation 
        v3 = torch.clamp_max(v2, 49.768) # Apply the clamp function with a maximum value of 49.768 to the previous output
        return v3

# Initializing model