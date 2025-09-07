
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.tensor([408967])
 
    def forward(self, v1):
        inv_scale  = (self.scale**(-1)).sqrt()
        v2  = torch.matmul(v1, v1.transpose(-2, -1)) / inv_scale
        return v2


# Initializing the model
m = Model()


# Inputs to the model
v3 = torch.randn(4096)
