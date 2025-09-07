
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3)
 
    def forward(self, x):
        v1 = self.linear(x) # Linear transformation with input of size (N, 1024) and output of size (N, 3) 
        v2 = v1 + 3 # Addition operation with input of size (N, 3) and constant `3`
        v3 = torch.clamp_min(v2, 0) # Clamp the addition to a minimum of zero
        v4 = torch.clamp_max(v3, 6) # Clamp the clamped value at 6
        return torch.div(v4, 6) # Divide by 6


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(256, 1024)
__output__  = m(x1)

