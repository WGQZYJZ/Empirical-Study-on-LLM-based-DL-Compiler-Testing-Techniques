
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self._other = 0
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self._other
        v3 = torch.relu(v2) # Apply the ReLU activation function to the result 
        return v3

# Initializing the model and its field
m  = Model2()
m._other = other


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
