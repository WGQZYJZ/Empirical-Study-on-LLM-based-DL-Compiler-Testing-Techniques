
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).float() * (-0.5 - v1) + ((~(v1 > 0)).float() * 1) * (v1)
        return v2


# Initializing the model and its parameters.
m = Model()
m_parameters = m.conv.weight, m.conv.bias