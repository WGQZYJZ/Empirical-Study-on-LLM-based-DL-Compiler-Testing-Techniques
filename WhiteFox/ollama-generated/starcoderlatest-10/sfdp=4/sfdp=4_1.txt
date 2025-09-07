
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention(8, 8)
 
    def forward(self, x1, x2):
        v1, _ = self.attn_layer(x1, x2, x2, attn_mask=None, key_padding_mask=None)
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
