
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) # applying the transposed convolution on input tensor
        v2 = torch.sigmoid(v1) 
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # randomly initialize an input tensor with shape (batch_size, num_channels, height, width). batch size can be 0. If batch size is zero, the network will not apply a batch normalization layer and it will fail the validation.
