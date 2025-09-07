
class Model(torch.nn.Module):
    def __init__(self, minv=0.5321867903470938, maxv=-0.8157794577073975):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(in_channels=32, out_channels=64, kernel_size=(1, 1), stride=2)
    
    def forward(self, x):
        v = self.deconv(x)
        minv = getattr(torch, 'clamp_' + self._target)(v, minv) 
        maxv = getattr(torch, 'clamp_' + self._target)(minv, maxv)
class Model(torch.nn.Module):
    def __init__(self, min_value=0.5321867903470938, max_value=-0.8157794577073975):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(in_channels=32, out_channels=64, kernel_size=(1, 1), stride=2)
 
    def forward(self, x):
        v = self.deconv(x) 
        minv = getattr(torch, 'clamp_' + self._target)(v, min_value) 
        maxv = getattr(torch, 'clamp_' + self._target)(minv, max_value)
