
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + self.__add_tensor__(v1, other=other)
     
    @staticmethod
    def __add_tensor__(t1, other):
        # Add the input tensor and the keyword argument to the output of the convolution
        # t1 : tensor, the output of a pointwise convolution, and "other" : torch.tensor, another tensor which is passed as a keyword argument in addition to the input tensor
        v2 = t1 + other
        return v2


# Initializing the model
m = Model(torch.randn(1, 3, 64, 64))
x1 = torch.randn(1, 3, 64, 64)
