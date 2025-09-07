
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            num_heads=8,
            key_dim=32,
            qkv_same_length=False,
            qkv_same_length_attention_mask=True,
        )
 
    def forward(self, query, key, value):
        v1, attn_weight = self.attn(query, key, value)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 8, 64, 64)
x2 = torch.randn(2, 8, 64, 64)
