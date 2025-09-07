
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.relu  = torch.nn.ReLU(inplace=True)
 
    def forward(self, x):
        v  = self.conv(x)
        return self.relu(v)


# Initializing the model
m  = Model()


