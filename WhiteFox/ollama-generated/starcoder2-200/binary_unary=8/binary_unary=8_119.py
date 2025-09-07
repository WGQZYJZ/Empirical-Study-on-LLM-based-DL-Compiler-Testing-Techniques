
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self._other_tensor
        v3 = F.relu(v2) # Use the ReLU activation function to compute the output of ReLU on the result
 
        return v3


m = Model()
m._other_tensor = torch.randn(1, 8, 64, 64)
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

# Inputs to the model: m._other_tensor and x1
