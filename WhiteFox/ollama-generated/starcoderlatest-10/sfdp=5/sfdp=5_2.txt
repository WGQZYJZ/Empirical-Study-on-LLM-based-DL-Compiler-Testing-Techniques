
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, n_head, d_model):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(n_head, d_model)
 
    def forward(self, q, k, v, attn_mask=None):
        return self.attn(q, k, v, attn_mask)[0]  # only need the first output


# Initializing the model
m = MultiHeadSelfAttention(8, 512)
q = torch.randn(32, 8, 64, 64)
k = torch.randn(32, 8, 64, 64)
v = torch.randn(32, 8, 64, 64)
attn_mask = None  # attention mask for the MultiHeadSelfAttention module


# Inputs to the model
