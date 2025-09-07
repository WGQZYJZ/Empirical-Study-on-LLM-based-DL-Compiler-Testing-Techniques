
class Model(torch.nn.Module):
    def __init__(self, splitsize=2000):
        super().__init__()
        self.splitsize  =  splitsize
 
    def forward(self, x1):
        v1  = torch.split(x1, [1,5], dim=3) # 1, 64x8x9
        v2  = v1[0] + v1[1] * 5
 
        return v2


m  = Model()

# Inputs to the model