
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v0  = self.linear(x1) # Apply a linear transformation to the input tensor
        v1  = (v0 + 3).clamp_min(0).clamp_max(6)/6 # Add `3` to the output of the linear transformation. Then clamp the output between 0 and 6, then divide by 6
        return v1

# Initializing the model
m  = Model()

