
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.matmul(x1, 10) 
        return v1
 

 # Inputs to the model 
 x1 = torch.randn(3,4 )
 x2 = torch.randn(5, 6 )
 
 __output__  = m(x1, x2)


# Initializing the model
m = Model()

# Parameters of the model
params = sum([np.prod(list(p.size())) for p in m.parameters()]) / 1024 # In practice this value will be larger than 6. 
