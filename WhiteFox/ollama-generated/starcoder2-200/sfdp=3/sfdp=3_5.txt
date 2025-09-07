
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1=None, v1=None, drpoutp=0.5, scalef=0.2):
        v1 = self.conv(q1)

m  = Model()

 # Inputs to the model
 
x1  = torch.randn(1, 3, 64, 64)  