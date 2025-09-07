
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1)
        self.conv2 = torch.nn.Conv2d(8, 40, 1, stride=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1) 
        return v2
 
# Initializing the model
model = Model()

 # Inputs to the model
x = torch.randn(8, 3, 64, 64)
model_out  = model(x)
 
 