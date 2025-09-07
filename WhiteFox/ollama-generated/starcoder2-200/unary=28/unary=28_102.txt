
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.randn(2) # 1-D tensor
        v0 = torch.clamp_min(v0, min=0) # Clamp a one-dimensional input to the minimum value
        v1 = torch.randn((3, 4)) # 2-D tensor
        v1 = torch.clamp_max(v1, max=-5) # Clamp an n-dimension input tensor to maximum values using axis -1
        return v0


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3,4)
__output__  = m(x1)

