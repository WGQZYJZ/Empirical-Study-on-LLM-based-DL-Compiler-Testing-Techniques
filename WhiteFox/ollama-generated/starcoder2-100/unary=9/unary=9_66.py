
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
         v1  = self.conv(x) 
         v2  = v1 + 3
         v3  = F.clamp_min(v2, min=0)
         v4  = torch.clamp_max(v3, max=6)
         return v4 / 6
 
 # Initializing the model
 m  = Model()
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 85, 79)

 # Initializing the input tensor for the model
 x2 = torch.zeros([1, 3, 84, 79]) + 10.0 
 
 # The outputs of the model are different from those obtained in the previous model example 
 y1  = m(x1)
 
 __output__  = m(x2)

