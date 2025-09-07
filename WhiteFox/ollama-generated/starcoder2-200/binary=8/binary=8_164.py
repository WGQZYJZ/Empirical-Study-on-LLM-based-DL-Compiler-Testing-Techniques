
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + torch.rand_like(v1).cuda()
        return v2


# Initializing the model and specifying which GPU to be used
m  = Model().cuda(0) # specify "device" as "cuda:0", or "cpu" if not in the GPU environment

