
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-7, max_value=0.3):
        super().__init__()
        self.linear  = torch.nn.Linear(64 * 64 * 3, 5)
 
    def forward(self, x2):
        v1  = self.linear(x2) 
        v2  = torch.clamp_min(v1, min_value=min_value) # Clamp the output of the linear transformation to a minimum value
        v3  = torch.clamp_max(v2, max_value=max_value) # Clamp the output of the previous operation to a maximum value 
        return v3


# Initializing the model
m1  = Model()

# Inputs to the model
x2  = torch.randn(48000, 64 * 64 * 3)
__output__  = m1(x2)
