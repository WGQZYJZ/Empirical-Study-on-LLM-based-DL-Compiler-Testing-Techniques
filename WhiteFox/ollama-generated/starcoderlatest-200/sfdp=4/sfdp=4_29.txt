
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 12)
 
    def forward(self, qk, v):
        attn_weight = self.attn(qk, v)[0]
        output = torch.einsum("bkhd,bhdj->bhdk", (attn_weight, v)) # Compute the dot product of the attention weights and the value
        return output


# Inputs to the model
qkv1 = torch.randn(4, 32, 64, 64)
