
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        l1  = self._linear(x1) # Applying linear transformation to the input tensor
        l2  = l1 + 3   # Adding 3 to the output of the previous operation 
        l3  = torch.clamp_min(l2, 0)    # Clamping minimum to zero
        l4  = torch.clamp_max(l3, 6) # Clamping maximum to six
        l5  = l4 / 6   # Dividing output by 6
        return l5
 
    def _linear(self): 
        return torch.nn.Linear()


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(32, 3)


