
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        # Perform a matrix multiplication of the inputs and the weights and add it to the input
        v1  = self.conv1(x)
        v2  = self.conv2(v1) * 0.5
        v3  = torch.erf(v2)
        v4  = v3 + 1
        # Perform a matrix multiplication of the result and the weights and add it to the input
        v5  = self.conv1(v2) * 0.7071067811865476
        v6  = torch.cat([v5, v4], dim=1)
        return v6

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
