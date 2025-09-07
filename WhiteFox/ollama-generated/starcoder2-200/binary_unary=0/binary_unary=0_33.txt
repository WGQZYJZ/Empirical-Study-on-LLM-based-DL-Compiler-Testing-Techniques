
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other  # A random tensor is added to the result of applying the pointwise convolution operation on a randomly generated input tensor 
        v4 = torch.relu(v3)
        return v5

# Initializing the model
m = Model()

