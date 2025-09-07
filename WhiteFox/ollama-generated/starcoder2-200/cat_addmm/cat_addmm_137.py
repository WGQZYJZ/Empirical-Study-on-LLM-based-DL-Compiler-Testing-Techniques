
class Model(torch.nn.Module):
    def __init__(self, dim=2048):
        super().__init__()
 
        self.mat1  = torch.randn([576, 3 * 9], dtype=torch.float) 
        self.mat2  = torch.randn([3*9, dim]) 

    def forward(self, x):
        v1  = torch.addmm(x, self.mat1, self.mat2)
        v2  = torch.cat((v1), -10) 
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn([576])

 ## Output of the model
