
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, query, key, value, scale_factor):
        v1 = self.attn(query, key, value, scale_factor)
        return v1

 # Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
