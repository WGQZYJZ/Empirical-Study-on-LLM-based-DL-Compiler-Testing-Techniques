
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=0.5):
        v1  = self._modules['linear'](x1) + other
        return torch.nn.functional.relu(v1).type_as(x1), 
