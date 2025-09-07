
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=2)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = torch.add(v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
input_tensor1 = torch.randn(20, 128, 64, 64)
