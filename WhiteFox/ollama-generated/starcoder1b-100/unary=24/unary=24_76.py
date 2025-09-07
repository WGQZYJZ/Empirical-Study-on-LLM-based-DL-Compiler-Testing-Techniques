
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        #v2 = (1 - abs(v1)) * v1
        #v3 = t1 > 0
        #t4 = torch.where(t2, t1, v3)
        return v1


# Initializing the model
m = Model()

