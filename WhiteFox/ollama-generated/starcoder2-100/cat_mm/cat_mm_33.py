
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
         v1  = self.conv(x1)
         v2  = v1.detach()
         return [v2]

 # Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
x2 = x1.clone().detach_() + torch.empty_like(0).random_(size=[3]).to(x1) # Dummy input tensors of the same shape as `x1`
 
# List of outputs from the model
__outputs__= m(x1, x2)

