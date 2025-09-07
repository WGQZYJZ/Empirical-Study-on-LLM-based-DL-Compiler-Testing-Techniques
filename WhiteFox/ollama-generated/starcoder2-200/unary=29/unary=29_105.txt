
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv_transpose(x1)
        v2  = torch.clamp_min(v1, min=0.9476314571869684)
        v3  = torch.clamp_max(v2, max=0.9531970324659377)
