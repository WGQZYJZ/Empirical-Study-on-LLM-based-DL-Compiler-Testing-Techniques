
class Model(torch.nn.Module):
    def __init__(self, num_layers=2):
        super().__init__()
        for i in range(num_layers):
            self.__setattr__("conv" + str(i), torch.nn.Conv2d(3 * 8, 8, 1, stride=1, padding=0))
 
    def forward(self, x1):
        v1 = None # type: torch.Tensor
        for i in range(2):
            v1 = self.__getattr__("conv" + str(i))(v1)
        return v1
 

# Initializing the model with one convolution layer
m1 = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3 * 8, 64, 64) # C / NCHW or NHWC
