
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1, other):
       v1  = self.conv(x1)
       return v1 + other

 # Initializing the model
 m = Model()

 # Inputs to the model and another tensor that's used as an argument in addition operation
 x1 = torch.randn(1, 3, 64, 64)
 other = torch.tensor([0])

 __output__  = m(x1, other)
