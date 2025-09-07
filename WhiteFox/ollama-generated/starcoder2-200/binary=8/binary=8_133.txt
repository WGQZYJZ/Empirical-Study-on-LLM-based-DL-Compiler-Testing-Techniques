
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) + other
        return v1


# Initializing the model
m  = Model()
other  = torch.randn(5, 64, 32, 32).to("cuda")
# Inputs to the model
x1 = torch.randn(10, 3, 384, 384)


__output__  = m(x1)

