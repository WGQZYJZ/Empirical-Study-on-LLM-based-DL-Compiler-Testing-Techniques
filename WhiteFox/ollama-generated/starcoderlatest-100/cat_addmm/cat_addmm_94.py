
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.nn.Parameter(torch.randn(32, 56).float())
        self.mat2 = torch.nn.Parameter(torch.randn(48, 72).float())
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2)
        return v1


# Initializing the model
m = Model()
print(m[0].shape) # The shape of weight matrix mat1
