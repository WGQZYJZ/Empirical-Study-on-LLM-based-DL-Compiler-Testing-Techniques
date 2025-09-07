
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x1):
        v0 = self.conv(x1) # Apply the convolution transpose layer to input tensor
        return torch.sigmoid(v0)


m  = Model()


x1  = torch.randn(1,8,64,64)# The model takes input with shape of (batch size, channels, height, width) as the input to the model


