
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.randn(8, 3, 32)
        self.mat2 = torch.randn(8, 3, 64)
 
    def forward(self, input):
        v1 = torch.addmm(input, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 64)
