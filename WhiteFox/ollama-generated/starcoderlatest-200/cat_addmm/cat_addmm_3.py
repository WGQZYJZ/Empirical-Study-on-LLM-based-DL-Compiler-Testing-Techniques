
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, x2)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
__input_0__ = torch.randn(3, 8, 64, 64) # input[dim=0] tensor must be consistent with x1 and dim=0 of mat1 or mat2
__input_1__ = torch.randn(5, 8, 64, 64) # input[dim=0] tensor must be consistent with x2 and dim=0 of mat1 or mat2
