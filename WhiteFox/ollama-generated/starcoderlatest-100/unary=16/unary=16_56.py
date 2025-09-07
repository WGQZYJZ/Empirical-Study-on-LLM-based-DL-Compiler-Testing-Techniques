
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8 * 64 * 64, 20)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = F.relu(v1.view(-1, 8 * 64 * 64)) # Apply the ReLU activation function to the output of the linear transformation
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
