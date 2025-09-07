
class Model(torch.nn.Module):
    def __init__(self, num=5):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.mm(x1, x2)
        t2 = torch.cat([t1] * 3 + [t1], dim=-1)

# Initializing the model
m  = Model()

 # Inputs to the model
    x1 = torch.randn(4096, 512)
    x2 = torch.randn(512, 8192)
 __output__  = m(x1, x2)
 
