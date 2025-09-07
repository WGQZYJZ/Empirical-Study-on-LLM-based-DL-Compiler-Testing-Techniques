
class Attention(torch.nn.Module):
    def __init__(self, hidden_size=768):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.1)
 
    def forward(self, query, key, value, attn_mask):
        v  = <EMAIL> - torch.triu(attn_mask, diagonal=1) * 1e9 + q
        w  = torch.softmax(v, dim=-1)
        o  = self.dropout(w @ v2)
        return o

