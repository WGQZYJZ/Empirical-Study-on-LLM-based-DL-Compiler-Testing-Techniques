
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # This model should be different from the previous one.
        v1 = torch.tensor([5., 6.], device="cuda") 
        v2 = x1.permute(0, 1) / v1[:, None]
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 4).cuda()
__output__  = m(x1)