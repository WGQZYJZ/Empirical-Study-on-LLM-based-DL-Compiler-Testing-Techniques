
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, x1, x2):
        qk = (x1 * x2).transpose(-2, -1) / math.sqrt(x1.size(-1))
        attn_weight, _ = self.attn(qk, None, x1, attn_mask=None)  # Apply MultiheadAttention to compute attention weights and values of the current position and context positions in key (i.e., 'key') and query (i.e., 'query').
        output = torch.matmul(attn_weight, x2)  # Compute a weighted sum of the value tensor based on the attention weights.
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
x2 = torch.randn(8, 3, 64, 64)
