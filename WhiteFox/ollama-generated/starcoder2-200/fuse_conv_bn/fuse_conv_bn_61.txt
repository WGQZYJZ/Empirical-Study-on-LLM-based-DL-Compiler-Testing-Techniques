
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 80, kernel_size=5) 
        self.bn = torch.nn.BatchNorm2d(80) 

    def forward(self, x1): # X can be 1 or 2 representing the dimension.
        v1  = x1.permute(0, 2, 1).contiguous()
        v2  = self.conv(v1) 
        v3  = torch.nn.functional.batch_norm(v2, running_mean=None, running_var=None, weight=self.bn.weight, bias=self.bn.bias, training=False)
        return v3

m = Model()

x1 = torch.randn(40, 3, 6, 7).cuda() # X can be 2 or 3 representing the dimension.

