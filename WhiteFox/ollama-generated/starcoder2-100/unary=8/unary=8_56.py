
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 7)
        self.conv2 = torch.nn.ConvTranspose2d(8, 3, kernel_size=7)
 
    def forward(self, x1):
        v1 = self.conv1(x1) 
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=-4095) # clamp the output of the addition operation to a minimum of -4095 and a maximum of 6
        v4 = torch.clamp(v3, max=6) 
        v5 = v1 * v4  
        v6 = v5 / 6 
        return v2, v4


# Initializing the model
m = Model()


# Inputs to the model