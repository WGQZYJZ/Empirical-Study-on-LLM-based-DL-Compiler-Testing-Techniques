
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v0  = torch.randn(x1.shape[0], x1.shape[-3] * x1.shape[-4], 64, 64).to('cuda') # Sample input of the model
        x2  = self.convt(v0)
        v3  = torch.clamp_min(x2, min_value=-5)
        v4  = torch.clamp_max(v3, max_value=15) 
        return v4
