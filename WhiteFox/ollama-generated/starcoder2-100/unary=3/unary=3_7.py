
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 5, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(64, 32, 1, stride=1, padding=1)
 
    def forward(self, x):
        v0 = F.relu(x)
        
        v1 = self.conv (v0)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2 + v0)

        return v3


# Initializing the model 
m = Model()

 # Inputs to the model
x = torch.randn(1, 3, 64, 64)
