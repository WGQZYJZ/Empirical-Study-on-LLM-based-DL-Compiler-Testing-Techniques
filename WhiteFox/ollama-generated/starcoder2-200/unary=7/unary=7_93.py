
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
         v1 = self.conv(x) 
         l1  = v1 .t() * clamp(min=-6 , max=9, l1 + 2)
         l2  = l1 / 3
         l4 = torch.max(l1, l2)
         return l4
 

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64 , 64)
 
