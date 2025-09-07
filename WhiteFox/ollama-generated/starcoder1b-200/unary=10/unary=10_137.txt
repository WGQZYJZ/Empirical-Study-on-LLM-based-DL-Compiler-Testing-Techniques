
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64*64, 256)
 
    def forward(self, x1):
        v1 = self.conv(x1).reshape((-1, 64*64))
        v2 = torch.relu(self.linear(v1)).reshape((-1, 8, 8))
        return v2


# Initializing the model
m = Model()


