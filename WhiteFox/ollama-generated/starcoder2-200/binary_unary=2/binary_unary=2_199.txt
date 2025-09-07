
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,x1):
       v0  = torch.randn([1,3,64,64])
       v1  = self.conv(v0)
       v2  = v1 - v1
       v2[v2<0] = 0
...
...
...
...
...
...

       return v2

