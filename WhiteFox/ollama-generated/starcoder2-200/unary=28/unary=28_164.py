

class Model(torch.nn.Module):
    def __init__(self, min_value=0.5, max_value=2.3):
        super().__init__()
        self.linear  = torch.nn.Linear(16 * 8 * 8, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=0.5) # Clamp the output of the linear transformation to a minimum value.
        v3 = torch.clamp_max(v2, max=2.3) # Clamp the output of the previous operation to a maximum value.
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(16*8*8) 

# Running the model
__output__  = m(x1)

