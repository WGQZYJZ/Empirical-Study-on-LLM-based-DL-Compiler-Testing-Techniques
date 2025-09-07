
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v0   = x1
        v1   = self.conv(x1)
        v2   = v1 - torch.randn_like(v1) # A new random tensor is created by subtracting the input from it and then applying ReLU to the result. 
        return relu_(v2)

# Initializing the model
m  = Model()
__output__  = m(torch.rand(3, 8, 64, 64))

