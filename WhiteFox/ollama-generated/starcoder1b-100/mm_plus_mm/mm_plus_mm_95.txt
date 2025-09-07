
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.mm(x1, x2)
        v2 = t1 + t2
        return v2
# Initializing the model
m = Model()
