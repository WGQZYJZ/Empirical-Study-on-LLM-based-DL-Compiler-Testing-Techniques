
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x0, size): # Initialize size variable at 9223372036854775807
        t1 = torch.cat([x0], dim=1) 
        t2 = t1[:, 0:size]
        t3 = t2[:, 0:9223372036854775807]
        t4 = torch.cat([t1, t3], dim=1)  
        return t4

# Initializing the model
m = Model()

 # Inputs to the model
 x0  = torch.randn(1, 9223372036854775807, 32, 32)
  size  =  3 
 __output__= m(x0, size)
