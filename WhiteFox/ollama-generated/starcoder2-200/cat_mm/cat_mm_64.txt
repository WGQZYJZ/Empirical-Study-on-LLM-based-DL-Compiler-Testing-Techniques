
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.matmul  = torch.mm
 
    def forward(self, x1, x2):
        v1  = self.matmul(x1, x2)
        v2  = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input1  = torch.randn(5, 8)
input2  = torch.randn(5, 9)

x3  = torch.zeros((7))
for i in range(7):
    x3[i] = m(input1, input2)[0][i]
__output__  = x3

