
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, x2):
        v1, v2 = self.attn(x1, x2, attn_mask=None)
        return v1

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(10,3,56,56)
x2  = torch.randn(10,3,56,56)

 __output__  = m(x1, x2)

