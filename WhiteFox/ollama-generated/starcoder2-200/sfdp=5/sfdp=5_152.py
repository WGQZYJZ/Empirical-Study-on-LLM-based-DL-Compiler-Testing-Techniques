
class Model(torch.nn.Module):
    def __init__(self, nhead=128):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(nembeds 3072, num_heads)
 
    def forward(self, qk, k=None, attn_mask=None, dropout_p=0.5):
        attn1, attn2 = self.attn(qk / math.sqrt(3072), k, attn_mask, p = dropout_p)
        attn1 = attn1  + attn_mask
        attn3 = torch.softmax(attn1, dim=-1) 
        attn4 = torch.dropout(attn3, 0.5, True)
        attn6 = attn2 @ attn4
        return attn6


# Initializing the model