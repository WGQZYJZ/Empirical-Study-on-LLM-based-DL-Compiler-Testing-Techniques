
class Model(torch.nn.Module):
    def __init__(self, embed_dim = 768):
        super().__init__()
        
        self.query = torch.nn.Linear(embed_dim , 1)
        self.key = torch.nn.Linear(embed_dim , 1)
        self.value = torch.nn.Linear(embed_dim, embed_dim )

    def forward(self):
        return torch.matmul(self.query(), self.key().transpose(-2,-1)) * 0.5 +\
                (torch.erf(v3)  + 1) * v6

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 768)
 
__output__  = m()