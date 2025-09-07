
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(256, 8)
 
    def forward(self, qk):
        attn_weight, _  = self.attn(qk)
        output = attn_weight @ value
        return output

# Initializing the model
m = Model()

 # Inputs to the model
    x1 = torch.randn(32, 256, 16, 16)
    k  = torch.randn(8, 256, 16, 16)
    v  = torch.randn(8, 256, 16, 16)
