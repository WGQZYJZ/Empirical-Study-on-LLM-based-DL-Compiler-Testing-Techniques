
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1 = torch.mm(input1, input2)
        v2 = torch.cat([v1] * 3, dim=0) 
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
i1 = torch.randn(16, 48, 48, 48)
i2 = torch.randn(1, 48, 3950, 3950)
__output__  = m(i1, i2)

