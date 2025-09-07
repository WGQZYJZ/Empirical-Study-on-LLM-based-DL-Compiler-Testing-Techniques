
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 2)
 
    def forward(self, qk, attn_mask):
        output, attention_weight = self.attn(qk, qk, qk, attn_mask=attn_mask)
        return output


# Inputs to the model
qk = torch.randn(4, 8, 16, 64)  # [batch size * query head, feature dimension, num key, key depth]
