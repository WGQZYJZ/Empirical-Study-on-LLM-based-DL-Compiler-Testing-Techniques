
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = torch.relu(v1)
        return v4


# Initializing the model
m2  = Model2()

# Inputs to the model
x2  = torch.randn(1, 3, 64, 64)
__output2__  = m2(x2)

# Generating new PyTorch models: 1. Use of self.apply()

# Model
class MyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        self.conv1  = torch.nn.Conv2d(3, 8, 3)
        self.apply(lambda m: setattr(m, 'running_mean', None))  # Clears running statistics for the conv layers in MyModule using self.apply()
        self.conv2  = torch.nn.Conv2d(8, 10, 5)
 
    def foo(self):
        self.conv1.forward(torch.randn(32, 3, 64, 64))
# Initializing the model
m_new = MyModule()

# Inputs to the model (randomly generated numbers)
x = torch.randn(50, 3, 64, 64)
y1= m_new(x)

