
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(16, 8)
 
    def forward(self, q, k, v, attn_mask=None):
        output, _ = self.attention_layer(q, k, v, attn_mask=attn_mask)
        return output


# Initializing the model
m = Model()
q = torch.randn(16, 16, 8, 4096)
k = torch.randn(16, 32, 8, 4096)
v = torch.randn(16, 16, 8, 512)


# Inputs to the model
attn_mask = torch.randint(1, (16, 1), device="cuda")  # The mask that decides whether or not we should attention between pairs of input tokens
