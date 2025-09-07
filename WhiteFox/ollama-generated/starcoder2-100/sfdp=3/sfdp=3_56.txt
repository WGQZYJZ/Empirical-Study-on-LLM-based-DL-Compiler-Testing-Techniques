
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att  = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)

    def forward(self, v0):
        v1, v2  = self.att(v0, v0, v0)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
v0  = torch.randn(3, 8, 512)
 
 __output__  = m(v0)

