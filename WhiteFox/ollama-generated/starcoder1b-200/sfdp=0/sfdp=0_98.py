
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        x  = F.relu(self.conv1(x))  # Apply relu
        x  = F.max_pool2d(x, 2, stride=2)  # Max pool with window size 2 and stride 2
        x  = self.conv2(x)        # Apply convolution with kernel size 1
        v1 = x  * 0.5  # Multiply the output of the first convolution by 0.5
        v2 = torch.tanh(self.conv1(x))  # Apply tanh to the second convolution
        v3 = v1  * 0.7071067811865476  # Multiply the output of the first convolution by 0.7071067811865476
        v4 = torch.erf(v3)  # Apply the error function to the second convolution's output
        v5 = v4 + 1  # Add 1 to the error function's output
        v6 = x  * v5  # Multiply the output of the first convolution by the error function's output
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
