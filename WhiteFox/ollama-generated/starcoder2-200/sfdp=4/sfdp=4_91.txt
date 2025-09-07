

class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(16, 32)
        self.key   = torch.nn.Linear(16, 32)
        self.value = torch.nn.Linear(16, 32)
    
    def forward(self, x): 
        # Inputs
        query = x
        key = query
        value = query
        attn_mask = None
        
        # Dot-product attention:
        qk = self.query(query) @ self.key(key).transpose(-2,-1) / math.sqrt(qk.size(-1))
        if attn_mask is not None:
            qk  = qk + attn_mask
        
        # Apply softmax to the result 
        attn_weights   = torch.softmax(qk, dim=-1)

        # Compute the dot product of the attention weights and the value tensor 
        output         = attn_weights @ self.value(value)
        
        return output


# Initializing the model