
class Model(torch.nn.Module):
    def __init__(self, ksize1 = None, ksize2=None, ksize3=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2): # The second input tensor is also a keyword argument to the convolution operation.
        v1  = self.conv(x1)  
        v2  = v1 + other  # Add another tensor to the output of the convolution.
        return v2


# Initializing the model and pass it two inputs:
m = Model()
