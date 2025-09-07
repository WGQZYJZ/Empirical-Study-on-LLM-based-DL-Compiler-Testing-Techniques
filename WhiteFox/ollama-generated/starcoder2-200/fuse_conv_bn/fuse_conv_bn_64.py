
class FusedModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvXd(2, 10, 3)
        self.bn = torch.nn.BatchNormXd(10)

    def forward(self, x1):
         v1 = self.conv(x1)
         v2 = self.bn(v1) 
         return v2

m_fused = FusedModel() # call the fused model API
__output__  = m_fused(x1) # run the fused model, which is equivalent to the original module.

