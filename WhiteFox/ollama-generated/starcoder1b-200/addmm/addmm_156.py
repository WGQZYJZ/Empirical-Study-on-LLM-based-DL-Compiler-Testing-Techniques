
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
        self.fc1  = torch.nn.Linear(4 * 8 * 8, 8 * 8 * 4)
 
    def forward(self, x1, inp):
        v1  = self.conv1(x1)
        v2 = v1  + inp  # Matrix multiplication with 'inp' and add to result of conv
        v3 = torch.mm(v2.view(-1, 4, 8 * 8), v2.view(-1, 8, 8))
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
inp  = torch.randn(1, 8 * 8 * 4)
__output__  = m(x1, inp)

