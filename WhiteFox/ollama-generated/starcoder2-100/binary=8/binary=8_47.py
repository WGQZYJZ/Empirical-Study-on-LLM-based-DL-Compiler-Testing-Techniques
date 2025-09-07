
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other 
        return v2


# Initializing the model
m_0 = Model(other=torch.zeros((3,), dtype=torch.float64))
m_1 = Model(other=torch.ones((3,), dtype=torch.float64))
__output__  = m_0(x1) + m_1(x1).view(-1, 8 * 72, 1596, 1)

