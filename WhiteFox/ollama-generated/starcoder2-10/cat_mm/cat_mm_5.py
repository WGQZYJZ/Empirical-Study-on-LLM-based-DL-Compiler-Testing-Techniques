
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.mm
 
    def forward(self, x1, y1):
        v0  = self.mm(x1, y1)
        v2  = torch.cat([v0] * len(v0), dim=0).view(-1)
# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(3768945, 54371)
y1 = torch.randn(203475, 54371)
 
 __output__  = m(x1, y1)