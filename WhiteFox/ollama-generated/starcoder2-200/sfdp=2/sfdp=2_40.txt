
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(256, 768)
 
    def forward(self, x1):
        v3 = x1[0] + x1[1]
        v4  = [v3 for _ in range(8)] # Repeat 8 times to create the output
        v5 = torch.cat(v4, dim=0).permute(2, 0, 1)
        v6 = self.qkv(v5) 
        return [v3]

# Initializing the model
m  = Model()

 # Inputs for the model 
x1  = torch.randn((8, 2))
  __output__   = m(x1)