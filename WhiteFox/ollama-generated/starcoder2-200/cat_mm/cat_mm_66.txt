
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.mm

    def forward(self, x1, y1):
        v0  = self.mm(x1,y1)
        return v0

 # Initializing the model
m = Model()
 
 # Inputs to the model
 
v1  = torch.randn(56789,2345, dtype=torch.float32)
v2  = torch.randn(2345,dtype=torch.float32)
