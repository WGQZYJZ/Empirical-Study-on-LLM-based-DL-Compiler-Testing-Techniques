
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + x1
        v2 = torch.relu(v1)
        return v2

# Initializing the model
m = Model2()

# Inputs to the model 
x1 = torch.randn(1, 3, 64, 64) # The input tensor does not need to be different from before

 __output__= m(x1)
 
- We do not check the initial values of the tensors; 