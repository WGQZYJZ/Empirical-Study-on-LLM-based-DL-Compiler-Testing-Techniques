
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.convt(x1) # Apply pointwise transposed convolution to the input tensor 
        v2  = torch.clamp_min(v1, min=0.) # Clamp the output of the transposed convolution to a minimum value
        v3  = torch.clamp_max(v2, max=7.5) # Clamp the output of the previous operation to a maximum value 
        return v3

# Initializing the model
m = Model()

