
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(3)
        v2  = torch.softmax(v1, dim=-1)
        v3  = v2.matmul(x1)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(480, 96, 7, 7).to('cuda:0')
x2  = torch.randn(480, 96, 7, 7).to('cuda:0')
__output__  = m(x1, x2)