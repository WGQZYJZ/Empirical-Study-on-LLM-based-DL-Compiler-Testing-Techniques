
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self,x1):
       v1  = self.conv(x1)
       v2  = v1 - other
       v4  = torch.relu(v2)
       return v4


# Initializing the model
m  = Model()

# Inputs to the model
other  = [torch.zeros(3,8,65,65),torch.randn(3,8,10,10),torch.zeros(3,8,79,4)]
x1     = torch.randn(1,3,65,65)
for i in range(len(other)):
    __output__  = m(x1)

