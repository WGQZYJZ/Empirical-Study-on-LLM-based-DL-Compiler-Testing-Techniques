
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3  = torch.nn.functional.conv_transpose2d(x1)
        v4  = v3 * 0.5
        v7  = v3  * 0.7071067811865476
        v9  = torch.erf(v7)
        v11  = v9 + 1
        v21  = self.__class__.conv_transpose(x1)
        v31  = v21 * v11
        return v4
 
m  = Model()
 
