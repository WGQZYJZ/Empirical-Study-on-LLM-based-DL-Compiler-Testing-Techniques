
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, w1, x2, y2, z2, w2):
        v1  = torch.mm(x1,y1) 
        v2  = torch.mm(z1,w1) 
        return v1 + v2
 
m  = Model()

