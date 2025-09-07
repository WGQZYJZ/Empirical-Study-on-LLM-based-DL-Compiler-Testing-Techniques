

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = torch.clamp_min(v1, min=-5) # clamping the output to a minimum value -5 is used as an example here
        v3 = torch.clamp_max(v2, max=5)# clamping the output of the previous operation to a maximum value 5 is used as an example here 
        return v3
