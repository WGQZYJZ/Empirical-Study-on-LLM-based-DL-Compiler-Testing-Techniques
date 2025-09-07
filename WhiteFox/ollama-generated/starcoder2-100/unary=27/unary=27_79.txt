
class Model(torch.nn.Module):
    def __init__(self, min_value=-100., max_value=500.)
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
       v1 = self.conv(x) 
       v2 = torch.clamp_min(v1, min_value) # Clamp the output of the convolution to a minimum value
       v3 = torch.clamp_max(v2, max_value) # Clamp the result of the previous operation to a maximum value
