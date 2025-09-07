
class Model(torch.nn.Module):
    def __init__(self, v1 = torch.Tensor([2])):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v0 = self.conv(x1) 
        v1 = -v0 # Subtract 'other' from the output of the convolution
        return v1


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1,3,64,64)
  