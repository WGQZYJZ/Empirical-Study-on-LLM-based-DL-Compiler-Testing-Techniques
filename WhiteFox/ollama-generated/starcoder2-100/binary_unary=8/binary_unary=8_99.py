
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=0)
 
    def forward(self,x1):
        v1  = self.conv(x1)
        v2  = v1 + t1 # the output of conv
        v4  = torch.relu(v2)# activation function 
        return v3


# Initializing the model