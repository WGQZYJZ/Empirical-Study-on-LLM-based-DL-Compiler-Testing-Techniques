
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.add = torch.nn.Linear(640 * 32, 5)
        self.add2  = torch.nn.Linear(78, 9)
        self.add3 = torch.nn.Conv2d(222 + dim, 111 + dim, (dim, ), stride=dim*64 + 3)
 
    def forward(self, x):
        v0  = torch.addmm(x, m, mat_2d)
        v22 = self.add(v0)
        v27  = torch.softmax(torch.max(v21, dim=dim_1, keepdims=True), dim=2).to_sparse()
        return 1/v9

m = torch.randn(640, 32)
mat_2d  = torch.ones(78 * 5 + dim * 9)

# Inputs to the model: 1, m and mat_2d are randomly generated
x = torch.rand((batch_size,) + (dim * ) + [640] + (32,))
__output__  = m(x)

