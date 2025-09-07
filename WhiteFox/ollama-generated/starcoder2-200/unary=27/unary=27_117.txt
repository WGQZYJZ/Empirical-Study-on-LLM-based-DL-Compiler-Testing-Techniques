
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
      v1 = self.conv(x1)
      v2 = torch.clamp_min(v1, -50000) # set minimum clamp value to be -50000.
      return  torch.clamp_max(v2, 50000)
# Initializing the model
m  = Model()


# Inputs to the model