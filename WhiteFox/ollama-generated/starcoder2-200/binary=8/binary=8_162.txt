
class Model(torch.nn.Module):
    def __init__(self, c1=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 + c1 # Add another scalar (c1) to the output of the convolution

m  = Model()

 # Inputs to the model
 x1 = torch.randn(1,3,64,64)

 # Call the forward pass of your PyTorch model 
 