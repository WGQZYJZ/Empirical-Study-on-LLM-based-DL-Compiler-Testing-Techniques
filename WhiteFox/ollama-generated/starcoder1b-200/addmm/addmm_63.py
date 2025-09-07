
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp):
        v1 = self.conv(x1)
        v2 = torch.mm(v1, inp) + inp  # Perform matrix multiplication on two input tensors and then add the result of this operation to another tensor 'inp'
        return v2


# Initializing the model
m = Model(torch.randn(1, 3, 64, 64))


