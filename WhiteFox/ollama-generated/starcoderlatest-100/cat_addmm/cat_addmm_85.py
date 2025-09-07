
class Model(torch.nn.Module):
    def __init__(self, dim = -1):
        super().__init__()
        self.mat1 = torch.randn(256, 3072).reshape((256, 8, 16)) 
        self.mat2 = torch.randn(194, 3072).reshape((194, 8, 16))
        self.input = torch.randn(1, 3072)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim = -1)
        return v2


# Initializing the model
m = Model()


