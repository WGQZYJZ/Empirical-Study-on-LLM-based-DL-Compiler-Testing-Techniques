
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x):
         v1  = self.conv(x)
         v2  = v1 + 3
         v3  = torch.clamp_min(v2,0).clamp_max(v3,6)/6
         return v3


# Initializing the model
m=Model()
__output__  = m(torch.randn(1,3,57,57))

## Input to the model
torch.tensor([[[-1.,-0.4,-0.8],[-2.,-2.,-0.9]],

       [[ 0.6, -0.4 ,  0.4],
       [-0.1 , -0.5 , -0.7]]])
