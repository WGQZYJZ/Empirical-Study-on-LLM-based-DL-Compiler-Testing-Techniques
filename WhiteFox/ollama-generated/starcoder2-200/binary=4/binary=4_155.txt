
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear(320, 8)(x1) # Apply a linear transformation to the input tensor and specify the number of output features as 8
        v2 = v1 + other_tensor  # Add another tensor (specified by the keyword argument "other") to the output of the linear transformation
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(5,320)
__output__  = m(x1)
 
