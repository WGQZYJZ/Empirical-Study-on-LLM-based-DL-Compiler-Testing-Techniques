
class Model(torch.nn.Module):
    def __init__(self, other1=None, other2=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        if not (other1 is None or other2 is None):
            raise RuntimeError("Both 'other1' and 'other2' were specified")
 
    def forward(self, x1):
        v1 = self.conv(x1)
        #if "other1" in kwargs:
           v3  = v1 + self.__kwargs__["other"] # Add the keyword argument to the output of the convolution
        return v6


# Initializing the model with different input tensors