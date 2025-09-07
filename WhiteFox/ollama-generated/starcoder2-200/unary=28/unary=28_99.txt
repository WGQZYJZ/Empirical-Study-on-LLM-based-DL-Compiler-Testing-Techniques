
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.nn.functional.linear(x1) # Apply a linear transformation to the input tensor
        v  = F.clamp(v, min=min_value, max=max_value) # Clamp the output of the linear transformation to minimum and maximum values
        return v

m  = Model()

