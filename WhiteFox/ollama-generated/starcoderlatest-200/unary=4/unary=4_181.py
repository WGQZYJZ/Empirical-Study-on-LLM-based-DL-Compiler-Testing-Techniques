
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(4096, 512)
 
    def forward(self, x1):
        v1 = self.conv(x1) # Convolution + activation function
        v2 = v1 * 0.5 # Linear transformation + activation function
        v3 = v2 * 0.7071067811865476 # Linear transformation + activation function
        v4 = torch.erf(v3) # Error function + activation function
        v5 = v4  + 1 # Addition + activation function
        v6 = v2 * v5 # Element-wise multiplication + activation function
        v7 = self.linear(v6.view(-1, 4096)) # Linear transformation
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
