
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3,8,1,stride=1, padding=0)

    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1,-5) # min value -5
        v3  = torch.clamp_max(v2,+7) # max value +7
        return v3

m = Model()
__output__= m(torch.randn(4,80))

