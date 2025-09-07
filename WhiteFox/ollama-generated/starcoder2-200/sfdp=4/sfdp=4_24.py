
class Attention(torch.nn.Module):
    def __init__(self, h=8):
        super().__init__()
        self.dense = torch.nn.Linear(h * 2, h)
 
    def forward(self, query, key, value):
        v1 = torch.einsum('bij,bkj->bik', query, key)
        v2 = math.sqrt(query.size(-1))
        v3 = v1 / v2
        v4 = self.dense(v3)
 
        mask_value  = -1e9 
        attn_mask = torch.empty((len(key), len(query)), device=key.device, dtype=torch.float).fill_(mask_value)
        attn_mask[:, key != value] = query.new(
            (
                len(key), 
                len(query[0]), 
            )
        ).normal_()
 
        attn_weight  = torch.softmax(v4 + attn_mask, dim=-1) 
        output = attn_weight @ value 
        return output

# Initializing the model
m = Attention()

 # Inputs to the model
 query  = torch.randn(8, 203497654043956) key  = torch.randn(1024, 8, 203497654043956) value = torch.randn(1024, 8, 203497654043956)
