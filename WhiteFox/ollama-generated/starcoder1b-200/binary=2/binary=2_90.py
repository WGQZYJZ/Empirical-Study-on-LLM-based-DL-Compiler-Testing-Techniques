The model above generates a 0 input to this function, and then subtracts it from an existing zero input. The pattern characterizes scenarios where the output of a pointwise convolution is subtracted by another tensor or scalar.

# Model
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, *args, **kwargs):
        v1 = self.conv(x1)
        v2 = v1 - other  # Subtraction of 'other' from the output of the convolution
        return v2


# Initializing the model with a value of other tensor (a scalar is also acceptable)
m = Model(torch.zeros(1))
__output__  = m(x1, other=torch.zeros(1))
