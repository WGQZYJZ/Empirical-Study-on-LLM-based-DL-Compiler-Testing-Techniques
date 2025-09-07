
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            embed_dim=32, num_heads=8)
 
    def forward(self, x1, x2):
        qk, attn_weight  = self.attn(x1, x2, x2,
                                        key_padding_mask=None, need_weights=True)
        return qk


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 32, 480, 512)
x2 = torch.randn(8, 32, 480, 512)
