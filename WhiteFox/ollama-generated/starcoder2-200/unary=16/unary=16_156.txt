
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.linear=torch.nn.Linear(9*9*8,1024)
 
    def forward(self,x1):
         v1 =  self.conv(x1)
         v2 = x1*v1
         v3 = torch.relu(v1)
         return v2,v3
 
 # Initializing the model
 m2= Model2()

 # Inputs to the model
 x1  = torch.randn(1,3,9,9)
 
# Outputs of the model:
v2,v3 =m2(x1)

