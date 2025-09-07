
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other_tensor # Subtracting a tensor 
        v3  = torch.relu(v2)   # ReLU
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
__input0__, __input1__ = torch.randn(4, 8, 64, 64), torch.randn(4, 8, 25)

