
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, x2)
        v2  = v1 + self.inp 
        return v2
 
# Initializing the model with an input tensor to be added in the matrix multiplication operation
inp = torch.randn([64])
m  = Model()

