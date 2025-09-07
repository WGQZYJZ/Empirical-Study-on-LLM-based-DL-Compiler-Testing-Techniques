

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = self.sigmoid(v1) # Apply the sigmoid function to the output of the convolution
        v3  = v1 * v2 
        return v3
