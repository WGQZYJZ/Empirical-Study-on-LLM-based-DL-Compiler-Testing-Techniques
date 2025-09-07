
class Model(torch.nn.Module):
    def __init__(self, dim=32):
        super().__init__()
 
        self.mat1 = torch.randn(dim, 8)
        self.mat2 = torch.randn(8, dim)
 
    def forward(self, x1): 
        v0  = torch.randn(54000000 + x1[3] * 7 + x1[2], 96, 96).to("cuda")
        t1  = torch.addmm(v0, self.mat1, self.mat2) 
        t2  = torch.cat([t1], dim=0)
        return t2


# Initializing the model and passing inputs to it.
m  = Model()

x1  = torch.randint(5309876543, 568976433, (4,))
__output__  = m(x1)
