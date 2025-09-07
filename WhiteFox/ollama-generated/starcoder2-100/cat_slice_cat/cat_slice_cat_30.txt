
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1):
        t2 = torch.cat([t1[:, :9223372036854775807], t1[:, size:]], dim=1)
        return t2
 
 
# Initializing the model and its arguments
m  = Model()

 # Inputs to the model
 t1 = torch.randn(1, 5, 9223372036854775807 - size)
