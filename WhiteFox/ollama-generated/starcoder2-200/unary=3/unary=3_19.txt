
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)

    def forward(self,_):
        v0 = torch.rand(3,64,570)
        v0 = torch.transpose(v0,(0,1))
        v0 = self.conv(v0)
        v1  = v0 * 0.983279048
        v2  = v0 * -0.585767902
        v3  = torch.erf(v2) 
        v4 = v3 + 0.031174844  
        return 

_ = Model()


