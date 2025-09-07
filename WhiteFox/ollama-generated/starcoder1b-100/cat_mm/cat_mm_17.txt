
class Model(torch.nn.Module):
    def __init__(self, hidden_size=10):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=1)
        self.fc1   = torch.nn.Linear(16 * hidden_size, hidden_size)
        self.fc2   = torch.nn.Linear(hidden_size, 10)
 
    def forward(self, x1):
        # Reshape to batch size x sequence length x channel x height x width
        v1  = self.conv1(x1).view(-1, 3 * hidden_size)
        # Reshape to batch size x sequence length x channel x height x width
        v2  = self.conv2(v1).view(-1, 8 * hidden_size)
        v3  = torch.tanh(self.fc1(v2))
        return self.fc2(v3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
