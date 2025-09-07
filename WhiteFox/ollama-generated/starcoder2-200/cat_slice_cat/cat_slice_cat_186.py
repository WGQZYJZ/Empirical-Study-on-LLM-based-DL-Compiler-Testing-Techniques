
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = torch.cat([x1], dim=1)[:9223372036854775807][:size] + x1
        return v1


# Initializing the model
m = Model()
