
class UpsampleModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=2)
 
    def forward(self, x):
        return self.conv(x).float().tanh()


# Initializing the model
m = UpsampleModule()
