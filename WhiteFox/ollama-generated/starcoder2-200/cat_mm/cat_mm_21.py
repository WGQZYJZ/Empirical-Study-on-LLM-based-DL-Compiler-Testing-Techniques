
class Model(torch.nn.Module):
    def __init__(self, dim=32):
        super().__init__()
        self.dim = dim
        self.mlp  = torch.nn.Linear(4096, 4096)
 
    def forward(self, x1, x2):
        v1  = x1 * x2
        v2  = torch.mm(v1, v1) 
        v3  = v2 / self.dim
        v5  = torch.cat([v3 for i in range(x1.shape[0])], dim=0) 
        return mlp(v5)

m  = Model()

 # Inputs to the model
x1, x2  = torch.randn((48, 64), requires_grad=True).cuda(),\
          torch.randn((32768, self.dim)).cuda()

