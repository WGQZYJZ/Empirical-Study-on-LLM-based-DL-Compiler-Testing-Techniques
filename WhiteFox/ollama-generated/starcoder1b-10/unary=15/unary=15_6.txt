
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.relu(self.conv(x1)) # Pointwise convolution + ReLU function (after first convolution operation), i.e., add ReLU function after first convolution operation
        return v1


# Initializing the model
m = Model()


