
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=32)
        super().__init__()
        self.linear  = torch.nn.Linear(4 * 8 * 8, 64)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1, 4*8*8)) # Apply a linear transformation to the input tensor
        v2  = torch.clamp_min(v1, min_value=0.1) # Clamp the output of the linear transformation to a minimum value
        v3  = torch.clamp_max(v2, max_value=32) # Clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model