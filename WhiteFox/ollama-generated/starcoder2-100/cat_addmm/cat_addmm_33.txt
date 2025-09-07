
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.mat   = torch.nn.Parameter(
            data       = torch.empty((4,4), device='cuda', requires_grad=True), 
            )

    def forward(self):
        v0  = (1. / 256.) * t1
        v0  = torch.round(v0) # round the output of the division operation to 3 decimal digits. In most cases, this is not necessary and it will not be checked.
        return v0


# Initializing the model with `dim` argument set as a 5-dimensional tensor.
m  = Model(1).to('cuda')


# Inputs to the model