
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.mm(x1, torch.randn(4, 3), m0=m1)
        return v2 + v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1000, 3, 5)
m2 = torch.randn(3, 4).cuda()
inp_tensor = torch.randn(78).to('cpu')
m1 = m2.to('cuda:0')

