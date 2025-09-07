
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(input1, 8, 1)
 
    def forward(self, x1):
        v1  = torch.mm(x1, self.conv(x))

# Initializing the model
m  = Model(torch.randn(3), 64).cuda()


# Inputs to the model
__output__  = m(torch.randn((3)).cuda())


