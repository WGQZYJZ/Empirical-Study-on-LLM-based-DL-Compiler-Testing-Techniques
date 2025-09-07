
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(64, 8)
 
    def forward(self, x):
        # Apply a linear transformation to the input tensor
        x = self.conv(x)
        # Apply the ReLU activation function to the output of the linear transformation
        return torch.relu(x)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
