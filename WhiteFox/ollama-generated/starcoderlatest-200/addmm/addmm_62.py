
class Model(torch.nn.Module):
    def __init__(self, inp: torch.Tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp=torch.tensor([1])):
        v1 = self.conv(x1)
        v2 = torch.mm(v1,inp)
        return v6


# Initializing the model
m = Model(torch.randn(3))

# Inputs to the model
__input_1__ = torch.randn(4, 5)
