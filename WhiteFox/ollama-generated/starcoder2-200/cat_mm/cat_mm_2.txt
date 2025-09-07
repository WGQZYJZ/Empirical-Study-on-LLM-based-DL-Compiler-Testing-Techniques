
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v4  = []
        for i in range(x1.shape[0]):
            v7 = self.conv(x1[i,:,:,:])
            v5  = torch.ones_like(v7) * i
            v8 = torch.cat([v7], dim=0).to("cpu")
            v4.append(v8)
        v9 = torch.stack(v4,dim=0).cuda()
        return v9


# Initializing the model
m  = Model().eval()


# Inputs to the model