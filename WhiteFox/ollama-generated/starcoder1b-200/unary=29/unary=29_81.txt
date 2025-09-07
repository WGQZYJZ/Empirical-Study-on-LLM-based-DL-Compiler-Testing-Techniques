
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0.1, max_value=5.0):
        v1 = self.conv(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)

# Initializing the model
m = Model()


