
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.conv(x)
        return self.relu(v1)


# Initializing the model