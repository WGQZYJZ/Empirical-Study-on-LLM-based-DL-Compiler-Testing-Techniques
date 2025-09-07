
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v0 = torch.cat([x1], dim=1)
        v0  = v0[:, 0:9223372036854775807]
        v1  = v0[:, 0:size]
 
        return torch.cat([v0, v1], dim=1)
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1 = [torch.randn(2,3),
      torch.randn(4,5)]
 
 x2 = [16]
 
 

__output_0__ = m(*x1,*x2)


