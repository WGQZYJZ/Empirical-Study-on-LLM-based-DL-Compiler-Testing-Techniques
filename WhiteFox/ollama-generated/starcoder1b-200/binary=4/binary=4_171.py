
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.linear = torch.nn.Linear(16, 4096)

    def forward(self, x):
        v = F.relu(self.conv(x)) # ReLU activation layer
        v = self.linear(v) # Linear transformation

        return v


# Initializing the model
m = Model()


