
class Model(torch.nn.Module):
    def __init__(self, ndim1=8):
        super().__init__()
        self.scale = 1./ndim1**0.5
        self.key = torch.randn(4, 768)
        self.query = torch.randn(32, 768)
        self.value = torch.randn(32, 4*768)
 
    def forward(self):
        v1 = torch.matmul(self.query, self.key.transpose(-2,-1)) / self.scale 
        v2 = v1.softmax(dim=-1)
        v3 = torch.bmm(v2[:,:,None,:],self.value[:,:,None])
        return v3


# Initializing the model 
m = Model()

# Inputs to the model
