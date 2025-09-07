
class Model(torch.nn.Module):
    def __init__(self, minv=None, maxv=None):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
        if minv is not None:
            self.minv = torch.tensor([minv])
        else:
            self.minv = torch.zeros((1,))

        if maxv is not None:
            self.maxv = torch.tensor([maxv])
        else:
            self.maxv = torch.ones((1, ))
 
    def forward(self, x):
        v  = self.linear(x) 
        v2  = torch.clamp_min(v, min=self.minv[0])
        v3  = torch.clamp_max(v2, max=self.maxv[0])
        return v3


# Initializing the model with default values for minimum and maximum values
m  = Model()
__output__  = m(x)
