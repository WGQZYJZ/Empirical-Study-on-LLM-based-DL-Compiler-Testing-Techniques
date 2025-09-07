
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.fc1 = torch.nn.Linear(64 * 64 * 3, 32)
        self.fc2 = torch.nn.Linear(32, 3)
 
    def forward(self, x):
        conv  = self.conv(x)
        fc1   = self.fc1(torch.flatten(conv))
        return self.fc2(fc1)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(3, 64 * 64 * 3, dtype=torch.float)
