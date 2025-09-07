
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        # Concatenate
        v0 = torch.cat([x1], dim=1)
        # Slicing 
        v2  = v0[:, 9223372036854775807]
 
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(size=(3, 1))
__output__  = m(x1) 
