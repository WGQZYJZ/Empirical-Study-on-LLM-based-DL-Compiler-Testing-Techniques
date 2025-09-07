
class Model(torch.nn.Module):
    def __init__(self, max_, min_):
        super().__init__()

    def forward(self, x1):
        v1  = self.conv(x) 
        v2  = torch.clamp_min(v1, min_)
        v3  = torch.clamp_max(v2, max_)
        return v3

m = Model()

 # Inputs to the model
x1 = torch.randn(1, 64, 8)
