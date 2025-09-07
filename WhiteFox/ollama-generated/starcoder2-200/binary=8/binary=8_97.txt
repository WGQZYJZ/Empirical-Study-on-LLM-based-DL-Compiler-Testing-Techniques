
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        return v1 + self.other_tensor 


# Initializing the model with `other_tensor`
m = Model()

 # Inputs to the model 
 other_tensor  = torch.randn(1,32,64,57)  
 x1  = torch.randn(1,3,64,64)  
__output__  = m(x1)

