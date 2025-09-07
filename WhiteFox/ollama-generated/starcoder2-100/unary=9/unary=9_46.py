
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = 6 * ((v1 / 6).round()) + (v1 % 6) # This is the ReLU6 activation function followed by a normalization operation
        return v4


# Initializing the model