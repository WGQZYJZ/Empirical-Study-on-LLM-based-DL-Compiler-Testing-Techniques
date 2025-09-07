
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.sigmoid(v1) # The sigmoid function is added here for aesthetic reasons
        v3 = v1 * v2 
        return v3


# Initializing the model