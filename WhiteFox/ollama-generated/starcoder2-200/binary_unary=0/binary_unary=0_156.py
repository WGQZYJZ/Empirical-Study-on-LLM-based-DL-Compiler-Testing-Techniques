
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v0 = torch.randn(x1.shape).to(x1.device) + 1e-7
        v1  = self.conv(v0)
        v2  = v1 + other
        v3  = torch.relu(v2) # Add ReLU to the result
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model, the shape of inputs should be different from the previous one. 
x0 = torch.randn(1, 3, 64, 64) + other
x2 = m(x1) 
