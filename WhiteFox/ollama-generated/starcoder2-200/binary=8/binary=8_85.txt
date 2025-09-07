
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v0 = self.conv(x)
        v1 = v0 + kwargs['other'] # <-- Addition operation has an additional argument
        return v1

m  = Model()
 
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(1, 8, 64, 64).mean().item() # <-- Average value of the output tensor
