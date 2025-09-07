
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # add 3 to the output of the convolution (ReLU6)
        v3  = torch.clamp_min(v2, 0) # clamp to a minimum value of 0 (ReLU6)
        v4  = torch.clamp_max(v3, 6) # clamp to a maximum value of 6 (ReLU6)
        v5  = v1 * v4 # multiply the output of the convolution by the clamped result (ReLU6)
        v6  = v5 / 6 # divide the output of the multiplication operation by 6 (ReLU6)
        
        return v6

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)