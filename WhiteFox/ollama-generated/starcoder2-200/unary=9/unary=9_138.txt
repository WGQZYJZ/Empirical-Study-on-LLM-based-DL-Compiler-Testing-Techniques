
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # Addition with constant
        v3  = torch.clamp_min(v2, 0) # Clamp the result to a minimum of zero
        v4  = torch.clamp_max(v3, 6) # Clamp the previous value to a maximum of six
        v5  = v4 / 6 # Division by constant (to normalize the values in the range [0-6])
        return v5


# Initializing the model
m1 = Model()
