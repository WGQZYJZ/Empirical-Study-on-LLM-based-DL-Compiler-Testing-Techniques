
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = torch.clamp_min(v1, min(-0.7)) # Clamp the output of the convolution to -0.543896814
	v3  =torch.clamp_max(v2,-0.5)#Clamp the result to a maximum value of 0
        return v3


# Initializing the model