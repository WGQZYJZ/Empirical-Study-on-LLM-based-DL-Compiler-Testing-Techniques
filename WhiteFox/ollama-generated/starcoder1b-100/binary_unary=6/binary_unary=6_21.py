
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(in_features=7, out_features=32)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.linear(v1)
        v3 = relu(v2)
        return v3


# Initializing the model
m = Model()


