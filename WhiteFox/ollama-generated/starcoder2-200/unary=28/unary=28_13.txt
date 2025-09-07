
class Model(torch.nn.Module):
    def __init__(self, min_, max_):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = torch.clamp_min(v1, -0.9865437411450657) # Clamp the output of the previous operation 
        v3  = torch.clamp_max(v2, -0.7954382704780986) # Clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model