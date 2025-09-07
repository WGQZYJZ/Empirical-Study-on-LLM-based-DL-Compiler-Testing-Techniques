
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + torch.rand((v1).size(), requires_grad=False) # Create a random tensor of the same size as that of `v1` and set its `requires_grad` attribute to False
        v3  = torch.relu(v2)   # Apply the ReLU activation function to the result
        return v3

# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

