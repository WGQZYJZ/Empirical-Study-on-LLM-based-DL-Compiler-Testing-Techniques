
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v1 = torch.mm(x1, y1)
        v2  = torch.cat([v1] * len(x), dim=0) 
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
__input__x  = torch.randn((len(x), 5))
__input__y  = torch.randn((4, 7))

# Run the model: compute the output using the inputs and initialize the gradient.
__output__, gradOutput  = m(__input__x, __input__y)

