

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v0 = self.conv(x)
        v1 = F.relu(v0 + x)
        return v1

# Initializing the model with some weights and biases
m  = Model()

 # Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
