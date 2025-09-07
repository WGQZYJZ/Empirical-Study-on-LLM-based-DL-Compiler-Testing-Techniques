
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m_first = Model()
m_second = Model(other=torch.randn(4))


# Inputs to the first model (note: using the same input tensor as for the first model): 
