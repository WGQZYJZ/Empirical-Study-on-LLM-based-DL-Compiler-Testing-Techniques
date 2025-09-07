
class Model(torch.nn.Module):
    def __init__(self, min_, max_)
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.clamp_min(v1, min=min_)
        return torch.clamp_max(v2, max=max_)


# Initializing the model
min_, max_= 0., 3500.
m  = Model(min_, max_)

 # Inputs to the model 
 x = torch.randn(1, 3, 64, 64) 
  __output__  = m(x)

