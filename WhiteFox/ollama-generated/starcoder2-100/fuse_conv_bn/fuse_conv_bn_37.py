
class ConvBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(3, 48, 7) # Convolution
        bn = torch.nn.BatchNorm2d(48) 
        output = bn(conv(x1)) # Apply batch normalization to the convolutional result

        return output


m  = ConvBnModel() # Initialize the model
x1 = torch.randn(30, 7, 96, 96)
