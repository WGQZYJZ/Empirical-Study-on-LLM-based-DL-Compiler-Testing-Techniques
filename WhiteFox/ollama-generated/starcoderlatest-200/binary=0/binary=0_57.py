
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other is None:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            raise ValueError("other must be provided when using another parameter to constructor of Model.")
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if self.training and other is not None:
            v2 = v1 + other
        return v6


# Initializing the model
m  = Model() # The value for "other" parameter to constructor of Model will be assigned to all conv layers in "Model".
             # For example, in the forward method of Model, every time a convolution layer is used by assigning it to the variable self.conv, 
             # if the model contains at least one additional parameter (other=) that has been provided at initialization time,
             # another tensor will be passed as an argument for this layer; therefore, it will be added to the output of the previous layer.

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
