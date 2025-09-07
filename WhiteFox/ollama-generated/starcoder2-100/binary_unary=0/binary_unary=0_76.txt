
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.other = torch.randn(10).view(-1, 1, 4, 5)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Pointwise convolution with kernel size 1 applied to the input tensor x1
        v2  = v1 + self.other # Add another tensor to the result of the convolution
        v3  = torch.relu(v2) # Apply ReLU activation function to the result of the convolution and addition
        return v3
