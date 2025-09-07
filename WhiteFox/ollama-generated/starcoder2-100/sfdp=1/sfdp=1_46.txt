
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=128, num_heads=4)
 
    def forward(self, x1):
         v1  = self.attn(x1, key_padding_mask=x1 == 0)
         return v1

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(256, 384)
 
# Running inference on the model
__output__  = m(x1)
