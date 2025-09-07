
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        
        self.mat1 = torch.randn([2048], requires_grad=True) 
        self.mat2  = torch.randn([768]) 
        self.dim = dim

    def forward(self, x1):        
        v1 = torch.addmm(x1, mat1, mat2)
        return v1.cat(dim)

# Initializing the model
m = Model()

 # Inputs to the model
v1  = torch.randn([350], requires_grad=True, device=cuda:0) 
 __output__  = m(__input__)

