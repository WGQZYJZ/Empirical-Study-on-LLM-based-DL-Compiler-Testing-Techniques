
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x1, mat1, mat2): 
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim=dim)


# Initializing the model
m  = Model()

# Inputs to the model
__input1__, mat1 = torch.randn(3, 4), torch.randn(4, 5)
mat2  = torch.randn(5, 6)
__output__  = m(__input1__, mat1, mat2)

