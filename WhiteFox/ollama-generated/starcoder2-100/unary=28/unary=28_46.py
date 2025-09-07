
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=512.):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = torch.clamp_min(v1,  min_value) # Clamp the output of the previous operation to minimum value 
        v3  = torch.clamp_max(v2, max_value)  # Clamp the output of the previous operation to a maximum value
        return v3

m = Model()

