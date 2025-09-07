
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=2.):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0.1, max_value=2.):
        v1 = self.conv(x1)
        return v1 * min_value + (max_value - min_value) * (1. / max_value).clamp_(min_value)


# Initializing the model
m = Model()


