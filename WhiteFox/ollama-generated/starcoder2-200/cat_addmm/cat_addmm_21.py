
class Model(torch.nn.Module):
    def __init__(self, in_channels=32, out_channels=64, kernel_size=11):
        super().__init__()
        self.linear  = torch.nn.Linear(in_channels * kernel_size ** 2,
                                      in_channels * kernel_size ** 2)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, mat1, mat2)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(32, 64)
mat1  = torch.randn(32, 8 * 9)
mat2  = torch.randn(32, 64* 8 )

__output__  = m(x1)