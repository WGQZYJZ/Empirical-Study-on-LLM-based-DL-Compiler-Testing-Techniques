
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, arg1=1., arg2=0.):
        v1 = self.conv(x1, arg1, arg2)
        v2 = torch.convert_element_type(v1, arg2)
        v3 = torch.cumsum(v2, dim=1)
        return v3


# Initializing the model
m = Model()

