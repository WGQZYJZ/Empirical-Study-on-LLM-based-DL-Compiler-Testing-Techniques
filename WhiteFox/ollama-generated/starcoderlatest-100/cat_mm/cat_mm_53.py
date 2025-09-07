
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.mm(x1, x2)
        t2 = torch.cat([t1, t1, 3*t1, ..., 5*t1])
        return t2


# Inputs to the model
x1 = torch.randn(64, 5, requires_grad=True).cuda()
x2 = torch.randn(64, 5, requires_grad=True).cuda()
