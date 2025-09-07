
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(4, 16)
 
    def forward(self, query, key, attn_mask):
        output, _ = self.attention(query, key, value=None, attn_mask=attn_mask, key_padding_mask=attn_mask)
        return output


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(4, 64, 128, 128)
