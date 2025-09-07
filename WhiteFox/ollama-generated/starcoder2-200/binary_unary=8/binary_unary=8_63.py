
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # add the other tensor to the output of conv
        return torch.relu(v2)


# Initializing the model
m  = Model()
m._parameters['other'] = torch.nn.Parameter(torch.randn(3, 8))
__output__  = m(x1)


