
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        mat1 = torch.randn(3072, 4096)
        mat2 = torch.randn(4096, 512)
        return torch.addmm(x1, mat1, mat2)


# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(32768, 3072)
# Output of the model
