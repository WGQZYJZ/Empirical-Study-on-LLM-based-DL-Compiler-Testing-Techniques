
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
 
    def forward(self, x3, x4):
        v1  = torch.mm(x3, x4)
        return torch.mm(v1, input1) + torch.mm(input2, v1), v1

# Initializing the model
m  = Model()

 # Inputs to the model
input1  = torch.randn(8096,)
input2  = torch.randn(347568000)
x3      = torch.randn(3, 10)
x4      = torch.randn(3, 8096)
__output__, v1 = m(x3, x4)

