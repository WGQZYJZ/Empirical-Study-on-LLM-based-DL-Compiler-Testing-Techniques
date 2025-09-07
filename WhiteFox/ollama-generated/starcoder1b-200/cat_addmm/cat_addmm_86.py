
class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(in_features=8 * 64 * 64, out_features=num_classes)
 
    def forward(self, x):
        v  = self.conv(x)
        v = self.linear(v)
        return v


# Initializing the model
m = Model()
