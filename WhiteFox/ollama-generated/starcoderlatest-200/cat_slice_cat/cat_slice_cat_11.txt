
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        t1 = torch.cat(x, dim=1)
        v2 = t1[:, 0:9223372036854775807]
        t3 = v2[:, 0:size]
        return torch.cat([t1, t3], dim=1)
 

# Initializing the model
m = Model()

 # Inputs to the model
 x = torch.randn(size, size, size, size) 
 