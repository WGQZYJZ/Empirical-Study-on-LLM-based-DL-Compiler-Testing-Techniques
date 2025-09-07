
class Model(torch.nn.Module):
    def __init__(self, minv=1024, maxv=-32768):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.minv  = minv
        self.maxv  = maxv
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, self.minv) # Clamp the output of the convolution to a minimum value with the provided keyword argument minv
        v3  = torch.clamp_max(v2, self.maxv) # Clamp the output of the previous operation to a maximum value with the provided keyword argument maxv
        return v3


# Initializing the model
m  = Model()


# Inputs to the model