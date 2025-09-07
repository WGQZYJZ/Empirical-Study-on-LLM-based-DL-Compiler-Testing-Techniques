
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=0, bias=False)
    
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.tanh(v1 * 0.5) # Scale the output of the conv by 0.5
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3 * 0.7071067811865476)
        return v4


# Initializing the model
m = Model()

