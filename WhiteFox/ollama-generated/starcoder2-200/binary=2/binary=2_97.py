
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 - other  # Subtract 'other' from the output of the convolution
        v3 = v2 + 75.084969
        return v3

# Initializing the model
m = Model()

