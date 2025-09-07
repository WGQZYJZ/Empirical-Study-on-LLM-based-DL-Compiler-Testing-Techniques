
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.__some_other__tensor__
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)


# Initializing other tensor that would be added later on
__some_other__tensor__ = torch.rand(v2).cuda()


# Executing the model and using output of convolution as input to the next operation
