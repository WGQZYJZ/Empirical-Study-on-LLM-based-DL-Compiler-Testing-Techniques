
class Model(torch.nn.Module):
    def __init__(self, in_, out_, mat1):
        super().__init__()
        self.in = in_ 
        self.out = out_
        self.mat1  = mat1

    def forward(self, x2):
      v0 = torch.addmm(x2, self.mat1) # 50-dim matrix addition (input 49 dimensions) + matrix multiplication 
      v0 = torch.cat([v0], dim=0) # Concatenate along dimension 0 
      return v0

# Initializing the model 
m  = Model(in_=1, out_=3, mat1=torch.randn(50, 49)) 

# Input to the model
x2 = torch.randn(50) # This is a 50-dim vector
