
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1,  y1, z1): 
        t1 = torch.mm(x1,  y1)
        t2 = torch.mm(z1,  self.conv3(t1))
        return t2


# Initializing the model