
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3,8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3,8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v0_29 = self.conv2(x)
        v0_24 = v0_29 + v0_27
        v0_16 = torch.relu(v0_25)
        return v0_18


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(3, 4, 90, 90) 

# Run model inference using your inputs and expected outputs
__output__  = m(x).tolist()

