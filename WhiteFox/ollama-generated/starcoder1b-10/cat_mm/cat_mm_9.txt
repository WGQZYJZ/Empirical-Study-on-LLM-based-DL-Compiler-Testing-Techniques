
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)  # Apply convolution to the first input tensor
        v2 = self.conv(v1)  # Apply convolution to the output of the previous layer
        return torch.cat([v1, v2], dim=-1)


# Initializing the model
m = Model()


