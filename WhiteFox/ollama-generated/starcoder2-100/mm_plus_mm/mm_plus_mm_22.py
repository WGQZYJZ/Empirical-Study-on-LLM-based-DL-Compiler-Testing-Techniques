
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, input3, input4):
         v0  = torch.mm(input1, input2)
         v1  = torch.mm(input3, input4)
         v2  = v0 + v1
         return v2

# Initializing the model with generated inputs
m = Model()
i1  = torch.randn(56, 9)
i2  = torch.randn(87, 9)
i3  = torch.randn(42, 9)
i4  = torch.randn(20, 9)
__output__  = m(i1, i2, i3, i4)

