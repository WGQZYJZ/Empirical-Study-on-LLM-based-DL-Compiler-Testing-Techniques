
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(40, 8)
 
    def forward(self, x2):
        v7 = self.l1(x2)
        v8 = v7 + 3
        v9 = torch.clamp_min(v8, 0) 
        v10= torch.clamp_max(v9, 6)
        return v10 / 6


# Initializing the model
m  = Model()

 # Inputs to the model
 x2  = torch.randn(3, 40)
 
 __output__  = m(x2)