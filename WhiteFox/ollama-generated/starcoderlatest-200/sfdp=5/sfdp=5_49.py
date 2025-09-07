
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.query_proj = torch.nn.Linear(dim, dim)
        self.key_proj   = torch.nn.Linear(dim, dim)
 
    def forward(self, q1, k1):
        query = self.query_proj(q1) # Project the input tensor to a dimension of size dim
        key    = self.key_proj(k1)   # ...and again
    
        qk = query @ key.transpose(-2, -1) / math.sqrt(dim)
        qk += 1
        
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        
        output = (attn_weight @ value).transpose(-2, -1) @ key
    
        return output


# Initializing the model
m = Model(dim=3072)
 
# Inputs to the model
q1  = torch.randn(batch_size, num_heads * head_dim, seq_len, input_dim) # (1, 8, 56, 1024)
k1  = torch.randn(batch_size, num_heads * head_dim, seq_len, input_dim) # (1, 8, 56, 1024)
v1  = torch.randn(batch_size, num_heads * head_dim, seq_len, hidden_dim) # (1, 8, 32, 768)
 
