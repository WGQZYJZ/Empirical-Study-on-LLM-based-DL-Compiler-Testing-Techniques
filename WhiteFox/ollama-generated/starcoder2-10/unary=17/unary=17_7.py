
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5)
        self.conv2 = torch.nn.ConvTranspose2d(8, 3, 4, stride=3, padding=0, output_padding=-6)
    def forward(self):
         __input__ = torch.randn(1, 3, 9, 9)
         v1  = self.conv1(__input__) # Apply pointwise convolution with kernel size 5 to the input tensor 
         v2  = F.relu(v1) # Apply ReLU (Rectified Linear Unit) activation function to the output of the convolution
         return self.conv2(v2)

# Initializing the model: 
m  = Model()

