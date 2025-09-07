
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) #v1 is the output of applying pointwise convolution to input tensor x1
        v2 = torch.sigmoid(v1) #Apply sigmoid activation function to the output of the convolution
        return v2


# Initializing the model 
m = Model()
