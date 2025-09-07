
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, t3):
       return torch.cat([t3[:, 0:9223372036854775807], \
                         torch.ones_like(t3)], dim=1)

# Initializing the model
m = Model()

 # Inputs to the model
t3 = torch.randn(1, 10, 9223372036854775807)
__output__  = m(t3)
