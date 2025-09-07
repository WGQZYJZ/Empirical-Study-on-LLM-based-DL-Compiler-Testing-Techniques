class Attention(torch.nn.Module):
    def __init__(self, d_model: int, attn_mask=None) -> None:
        super().__init__()
        self.d_model  = d_model
 
    def forward(self, query, key, value):
        # Compute the dot product of the query and key 
        # plus an attention mask if provided (in this example we do not use this mask).
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        
        attn_mask  = torch.nn.Parameter(torch.empty([8], device='cuda'))
        torch.nn.init.normal_(attn_mask)
        
        attn_weight  = torch.softmax(qk + attn_mask, dim=-1)
        
        # Compute the dot product of the dropout output and value
        v  = attn_weight @ value
        return v
