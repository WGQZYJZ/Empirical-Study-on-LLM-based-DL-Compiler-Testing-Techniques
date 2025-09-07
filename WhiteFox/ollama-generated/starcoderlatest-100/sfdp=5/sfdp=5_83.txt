
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_scale = torch.nn.Parameter(torch.tensor(1e-2))
 
    def forward(self, qk, attn_mask, dropout_p):
        v1 = qk @ key.transpose(-2, -1) / math.sqrt(qk.size(-1)) + attn_mask
        v2 = torch.softmax(v1, dim=-1)
        v3 = self.attn_scale * torch.dropout(v2, dropout_p, True)
        output = (v3 @ value).transpose(-2, -1)  # Apply the attention weight to the value
        return output

# Initializing the model
m = Attention()


