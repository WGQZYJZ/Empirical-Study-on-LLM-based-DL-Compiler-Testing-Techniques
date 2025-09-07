
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attn = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, key, query, attn_mask):
        attn_weight, _ = self.multihead_attn(x1, key, value=key,
                                             padding_mask=attn_mask,
                                             batch_first=True)
        output = torch.mul(attn_weight, query)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key = torch.randn(1, 3, 64, 64)
query = torch.randn(1, 8, 64, 64)
attn_mask = torch.ones(1, 3, 64, 64).type(torch.float32)
