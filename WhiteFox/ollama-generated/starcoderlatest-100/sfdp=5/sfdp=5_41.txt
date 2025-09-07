
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=512, nhead=8):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(hidden_dim, nhead)
        self.dropout = torch.nn.Dropout(p=0.3)
 
    def forward(self, x1, x2, attn_mask=None):
        if attn_mask is None:
            attn_mask = torch.eye(x1.shape[-1], dtype=torch.float, device=x1.device).unsqueeze(-2) # (batch, head, query, key)
 
        qk = self.attn(x1, x2, x2, attn_mask)[0]
        output = torch.einsum('bhid, bidh -> bhid', qk, x2)  # (batch, heads, seq_len, dim)
        return output


# Initializing the model
m = Model()

