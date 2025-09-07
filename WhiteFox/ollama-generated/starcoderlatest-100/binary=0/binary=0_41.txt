
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_tensor = other_tensor
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if self.training:
            v2 = v1 + self.other_tensor
        else:
            v2 = v1
        return v2


# Initializing the model
m = Model()

# Input to the model when training is True
__input_for_training__  = torch.randn(1, 3, 64, 64)
__other_tensor__           = torch.randn(1, 8, 64, 64)
m = Model(__other_tensor__)
# Input to the model when training is False
x1 = __input_for_training__ 

