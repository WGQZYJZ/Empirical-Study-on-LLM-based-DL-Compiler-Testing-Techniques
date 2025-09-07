
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Conv2d(3, 64, kernel_size=1)
        self.m2 = torch.nn.Conv2d(64, 512, kernel_size=1)
 
    def forward(self, x):
        v1 = self.m1(x)
        v2 = self.m2(v1)
        return v2
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
