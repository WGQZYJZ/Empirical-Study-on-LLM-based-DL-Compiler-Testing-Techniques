

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.concat = torch.nn.Cat()
 
    def forward(self, t1, size):
        v1 = self.concat([t1])
        v2  = v1[:, :, :size]
        v3 = v2[:, :, :size]
        v4 = torch.cat([v1, v3], dim=0) 
        return v4

# Initializing the model
m = Model()

 # Inputs to the model
t1 = torch.rand(9223372036854775807) 
t2 = 34 # size
__output__  = m(t1, t2)

