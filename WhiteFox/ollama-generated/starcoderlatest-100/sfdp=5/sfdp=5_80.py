
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(num_heads=8, embed_dim=32)

    def forward(self, q1, k1, v1):
        _, _, attn_weight  = self.attn(q1, k1, v1, key_padding_mask=True)
        attn_weight = torch.nn.Dropout(attn_weight, p=0.5) # dropout is applied here
        output  = torch.matmul(attn_weight, v1) # dot product between attention and value
        return output


# Initializing the model
m = Model()
q1 = torch.randn(1, 8, 64, 64)
k1 = torch.randn(1, 8, 64, 64)
v1 = torch.randn(1, 8, 64, 64)
# Inputs to the model
