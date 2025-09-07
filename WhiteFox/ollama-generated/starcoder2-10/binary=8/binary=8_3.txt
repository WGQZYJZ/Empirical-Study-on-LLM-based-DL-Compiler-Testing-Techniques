
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other

    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = v1 + self.other # Adding self.other to the output of a convolution is okay!
        return v2


# Initializing the model with additional input tensor