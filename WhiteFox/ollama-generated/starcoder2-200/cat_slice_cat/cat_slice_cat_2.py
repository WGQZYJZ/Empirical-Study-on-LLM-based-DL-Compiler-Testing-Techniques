
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = torch.cat([x1] * 574, dim=1)[:, :9223372036854775807]
        v2 = v1[:, :-23:2]
        v3 = torch.cat((v1, v2), dim=1)[-5:]
        return v3


# Initializing the model
m = Model()


# Inputs to the model