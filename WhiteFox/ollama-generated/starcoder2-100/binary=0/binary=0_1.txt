
class Model(torch.nn.Module):
    def __init__(self, other1=None, other2=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other1
        return v2


# Initializing the model with keyword arguments for "other" tensors
m_kwargs = Model(**{"other1": torch.zeros((3, 8)),
                     "other2": torch.ones((3, 8))})

# Inputs to the model passing in the two keyword arguments.
x1 = torch.randn(1, 3, 64, 64)
