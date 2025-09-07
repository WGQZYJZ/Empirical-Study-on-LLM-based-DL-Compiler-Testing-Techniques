
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v4  = torch.cat([v1] * 5, dim=0)

        return v4

# Initializing the model
m  = Model(torch.randn(3, 3), torch.randn(3))

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
__output__  = m(x1, x2)



