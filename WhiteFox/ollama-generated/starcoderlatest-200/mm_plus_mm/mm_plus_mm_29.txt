
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.pool = torch.nn.MaxPool2d(2, 2)
        self.conv2 = torch.nn.Conv2d(8, 16, 3)
 
    def forward(self, x1):
        v1 = self.pool(torch.nn.ReLU()(self.conv1(x1)))
        v2 = torch.nn.MaxPool2d(4, 4)(v1)
        v3 = self.pool(torch.nn.ReLU()(self.conv2(v2)))
        return v3
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
