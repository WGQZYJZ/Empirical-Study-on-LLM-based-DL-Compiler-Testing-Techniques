
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other # another tensor
        return torch.relu(v2)


# Initializing the model and getting the output of the first forward pass with a batch size=3, input channel number=8, and input shape [64, 64] for the given `x1` data 
other = torch.randn((3, 8), dtype=torch.float) # another tensor
m    = Model()
