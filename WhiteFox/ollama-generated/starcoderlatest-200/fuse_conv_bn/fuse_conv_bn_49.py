
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @torch.jit.unused # This method is not used in the model graph and thus ignored during compilation
    def forward(self, input_tensor): 
        return self.conv1(input_tensor) 

    def conv1(self, x): 
        conv = torch.nn.functional.conv2d(x, self.w1, self.b1)
        bn = torch.nn.BatchNorm2d(...) # The batch norm layer will not be included in the model graph because it is an input node of the convolution layer
        return bn(conv) 


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 32, 32)
