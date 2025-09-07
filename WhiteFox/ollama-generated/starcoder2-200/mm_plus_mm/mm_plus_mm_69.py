
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.functional.linear # Linear transformation
        self.mm2 = torch.nn.functional.linear # Linear transformation
 
    def forward(self, x3, x4, y0):
        v5  = self.mm1(y0) + self.mm2(y0)
#         print('v5: ', type(v5))
 
        v7   = self.mm2(x4) 
        v6 = torch.mm(y0, x3)
        v8 = self.mm2(y0) 
        v9  = v7 + v6
        v10 = v9 + v8 
        v11 = v5 + v10 
#         print('v11: ', type(v11))
 
        return v11
 
 # Initializing the model
 m = Model()

 # Inputs to the model 
 x3, x4 = torch.randn(128, 67), torch.randn(59, 50)
  y0    = torch.zeros((3, 1))
 
 __output__  = m(x3, x4, y0)

 