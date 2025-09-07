
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 5, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x) + other
        v2 = self.conv2(v1) + other
        v3 = torch.relu(v2)

# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
 
