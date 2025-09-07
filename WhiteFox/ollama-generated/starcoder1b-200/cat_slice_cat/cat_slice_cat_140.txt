
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 5, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.cat([v1[:, :, 1:13] * 0.25,  # Select the output of the first convolution in the feature map
                           v1[:, :, -1:]], dim=1)
        v3 = v2 + self.conv2(x1[:, :, :-1])
        return v3


# Initializing the model
m = Model()


