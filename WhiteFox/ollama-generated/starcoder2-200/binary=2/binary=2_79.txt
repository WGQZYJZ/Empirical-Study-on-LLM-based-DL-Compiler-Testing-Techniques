
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        # Assign 'other' to the module attribute named 'other'. This is a trick for generating multiple versions of the same model with different input tensors.
        setattr(self, 'other', other)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - getattr(self, 'other')

        return v2


# Initializing the model and assigning another tensor for the 'other' attribute of the model
m = Model(torch.randn(3))  # Assigning a tensor to the 'other' module attribute.

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

