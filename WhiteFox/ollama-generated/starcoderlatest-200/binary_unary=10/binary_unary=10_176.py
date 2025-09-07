
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64*64, 32)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Apply a convolution with kernel size 1 and strides 1, then apply BatchNorm2d and ReLU to the output of the convolution
        v2 = v1 + other_tensor # Add another tensor to the output of the convolution
        v3 = torch.nn.ReLU()(v2)
        return v3
 

# Initializing the model
m = Model()


