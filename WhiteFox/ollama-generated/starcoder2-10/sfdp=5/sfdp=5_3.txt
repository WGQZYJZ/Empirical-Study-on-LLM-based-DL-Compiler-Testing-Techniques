
class MultiheadAttention(torch.nn.Module):
    def __init__(self, dim=768, heads=12, attn_dropout=0.1, dropout=0.1):
        super().__init__()
 
        self.heads  = heads
        self.scale  = math.sqrt(dim)
        
        self.query = torch.nn.Linear(dim, dim) 
        self.key   = torch.nn.Linear(dim, dim)
        self.value = torch.nn.Linear(dim, dim)
 
        self.attn_dropout = torch.nn.Dropout(attn_dropout)
 
    def forward(self, query, key, value, attn_mask=None):  
        q  = self.query(query).reshape(query.size()[0], self.heads * self.scale, -1)
        k  = self.key(key).reshape(key.size()[0], self.heads * self.scale, -1) 
        v  = self.value(value).reshape(value.size()[0], self.heads * self.scale, -1)
        
        # Compute the dot product of the query and key
        qk = torch.einsum("abc, bcd->abcd", (q, k)) / math.sqrt(self.scale) 
        
        # Add an attention mask to the scaled dot product
        if attn_mask is not None:
            attn_mask  = attn_mask.unsqueeze(0).expand(query.size()[0], -1, qk.size(-2), qk.size(-1))
            attn_mask  = (1.0 - attn_mask) * -1e9
        qk += attn_mask
        
        # Apply softmax to the result 
        attn_weight  = torch.softmax(qk, dim=-1) 
         
        # Apply dropout to the softmax output
        attn_weight  = self.attn_dropout(attn_weight)

        # Compute the dot product of the attention weights and value
        output = torch.einsum("abd, bcd->acd", (attn_weight, v))
        
        return output.reshape(*query.size(), -1), attn_weight


m  = MultiheadAttention()
