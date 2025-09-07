
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(512, 3)

    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        v2 = torch.mm(x3, x4) # Matrix multiplication between input3 and input4
        v3 = v1 + v2 # Addition of the results of the two matrix multiplications
        return self.mm(v3)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(50, 64, 512).cuda()
x2 = torch.randn(50, 512, 3).cuda()
x3 = torch.randn(50, 512, 3).cuda()
x4 = torch.randn(50, 3, 512).cuda()
__output__  = m(x1, x2, x3, x4)

