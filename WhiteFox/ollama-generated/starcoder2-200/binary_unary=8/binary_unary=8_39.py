
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self._conv(x1)
        v2  = torch.max(v1, torch.zeros(*v1.shape).to(x1))
        v3 = torch.sum(v2)
        return v3


# Initializing the model