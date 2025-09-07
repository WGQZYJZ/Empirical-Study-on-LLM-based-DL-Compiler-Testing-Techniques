
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.__init__.other # __init__.other is a tensor passed as keyword argument to the addition operation
        return v2


# Initializing the model and passing keyword arguments
m  = Model()
other_tensor = torch.randn(3, 8, 56, 56)
m.__init__.other = other_tensor # Initialize a tensor passed as keyword argument to the addition operation with another tensor
 
