
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, inp) # 1
        v2 = v1 + self.inp    # 3
        return v2

m = Model()
x1 = torch.randn([640])
