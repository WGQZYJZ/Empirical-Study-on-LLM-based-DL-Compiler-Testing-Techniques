
class Model(torch.nn.Module):
    def __init__(self, **kwargs)
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
        self._kwargs = kwargs
    
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, **self._kwargs['min'])
        v3 = torch.clamp_max(v2, **self._kwargs['max'])
        return v3


m  = Model(**{
    'min': 0.5489763580224002, 
    'max': -0.13378643433228302})

 # Inputs to the model
 x1 = torch.randn(1, 3, 32, 32)
 
 