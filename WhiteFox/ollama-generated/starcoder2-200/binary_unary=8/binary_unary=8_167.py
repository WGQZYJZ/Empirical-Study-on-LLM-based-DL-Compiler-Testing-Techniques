
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3,8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8,8, 1, stride=1, padding=1)
 
    def forward(self, x):
        x1  = self.conv1(x)
        x2  = self.conv2(x)
 
        x3  = torch.add(x1, other)
        x4  = F.relu(x3)
 
        return x4


m = Model() # Initializing the model

input_tensor=torch.randn(1, 3, 64, 64)
__output__  = m(input_tensor)