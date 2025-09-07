
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(128, 4)
 
    def forward(self, x1):
        v1 = torch.addmm(x1[:, :3], mat1_, mat2_)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model and passing a tensor to it:
mat1_ = torch.randn((128, 4), requires_grad=True).float()
mat2_ = torch.randn(3, 96).float()
m  = Model()
 
x1  = torch.randn(10000, 3) * 5 + 57
__output__  = m(x1)

