
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.functional.mm
 
    def forward(self, x1, y2):
        v0  = self.mm(x1,y2) 
        return v0


# Initializing the model
m  = Model()
m.cuda()
 
 # Inputs to the model
x1  = torch.randn(4867533, 50).cuda().float()
y1  = torch.randn(92, 50).cuda().float()


# Outputs from the model
output1  = m(x1, y1)

