
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1

class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1 + other_tensor) # <<< this is what we want to look for!
        return v1

# Initializing the model with random tensors as inputs and output tensors (in order to trigger the pattern).
m  = Model()

x1  = torch.randn(2, 3, 64, 64)
y1  = m(x1)

other_tensor = torch.randn(3, 8, 10, 10) # <<< this is what we want to find!

m2 = Model2()
__output__   = m2(x1)

