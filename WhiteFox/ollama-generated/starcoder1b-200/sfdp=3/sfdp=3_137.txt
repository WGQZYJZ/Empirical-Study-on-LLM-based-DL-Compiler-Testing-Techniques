
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale_factor = None
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if self.scale_factor is not None:
            v1  *= self.scale_factor
 
        return v1


# Initializing the model
m = Model()

