
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 0 # Add 0 to the output of the previous convolution (before relu activation function is applied)
        return torch.relu(v2)


# Initializing the model
m = Model()

