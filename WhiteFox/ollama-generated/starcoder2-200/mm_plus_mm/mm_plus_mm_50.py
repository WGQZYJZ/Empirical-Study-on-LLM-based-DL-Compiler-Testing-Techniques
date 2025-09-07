

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.functional.mm
 
    def forward(self, input1, input2, input3, input4):
        v1  = self.mm(input1, input2)
        v2  = self.mm(input3, input4) 
        v3  = v1 + v2
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
 
i1  = torch.randn(640, 857)
i2  = torch.randn(914, 520)
i3  = torch.randn(749, 873)
i4  = torch.randn(722, 970)
 
__output__  = m(i1, i2, i3, i4)

