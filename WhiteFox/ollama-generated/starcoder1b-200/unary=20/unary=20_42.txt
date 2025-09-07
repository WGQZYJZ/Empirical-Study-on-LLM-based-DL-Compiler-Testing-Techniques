
class Upsample(nn.Module):
    def __init__(self, factor=2):
        super().__init__()
        self.factor = factor
 
    def forward(self, x1):
        v1 = nn.functional.interpolate(x1, scale_factor=self.factor)
        v2 = torch.sigmoid(v1)
        return v2


class Decoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.upsample = Upsample()
 
    def forward(self, x1):
        v1 = self.upsample(x1)
        return v1


# Initializing the model
d = Decoder()
m = Model()


