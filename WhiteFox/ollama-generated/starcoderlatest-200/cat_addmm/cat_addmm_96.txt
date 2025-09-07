
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.tensor([[[1], [2], [3]], [[4], [5], [6]]])
        self.mat2 = torch.tensor([[[7], [8], [9]], [[10], [11], [12]]])
 
    def forward(self, x1):
        v1  = torch.addmm(x1, self.mat1, self.mat2)
        v2  = torch.cat([v1], dim=-1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
