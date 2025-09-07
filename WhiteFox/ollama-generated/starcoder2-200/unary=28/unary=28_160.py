
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2 = torch.clamp_min(v1, min=0.5) # 0.5 is the minimum value for the clamp function
        return torch.clamp_max(v2, max=32.5) # 32.5 is the maximum value for the clamp function


# Initializing the model and setting the minimum and maximum values for clamping operations
min = 0.4 # 0.4 is the minimum value for the clamp functions
max = 1.8 # 1.8 is the maximum value for the clamp functions
m  = Model() 


# Inputs to the model