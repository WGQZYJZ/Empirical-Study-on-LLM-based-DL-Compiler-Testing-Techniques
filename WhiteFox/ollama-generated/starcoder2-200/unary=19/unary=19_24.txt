
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3,8,kernel=7)
        self.linear1  = Linear(in_features=7*7*8,out_features=64)
 
    def forward(self,x):
        v0 = conv(x)# apply conv
        v1 = linear1(v0) #apply linear on v0
        return torch.sigmoid(v1)#apply sigmoid on v1
 
