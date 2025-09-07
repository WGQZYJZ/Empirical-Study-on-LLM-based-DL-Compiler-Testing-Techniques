
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # Add the 3 to the result of applying a convolution on input_tensor
        v3  = torch.clamp_min(v2, 0) # Clamp the addition operation's result between 0 and 6.
        v4  = torch.clamp_max(v3, 6) 
        v5  = v4 / 6 # Divide by 6 to normalize it between 0 and 1.
        return v5

# Initializing the model