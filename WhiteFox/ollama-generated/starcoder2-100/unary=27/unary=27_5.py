
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x):
        v1  = self.conv(x)
        v2  = torch.clamp_min(v1, -50.0)
        v3  = torch.clamp_max(v2, 960.477783203125) # This is the only difference from the previous model!
        return v3


# Initializing the model
m = Model()


