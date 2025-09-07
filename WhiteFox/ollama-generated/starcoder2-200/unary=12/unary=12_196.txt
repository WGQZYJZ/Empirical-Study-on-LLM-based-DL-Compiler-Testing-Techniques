
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1) # sigmoid activation function
        v3 = v1 * v2 # multiply the output of the convolution by the output of the sigmoid function
        return v3

# Initializing the model