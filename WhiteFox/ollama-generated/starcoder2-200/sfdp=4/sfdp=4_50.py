
class Attention(torch.nn.Module):
    def __init__(self, attn_dim=512):
        super().__init__()

        self.query = torch.nn.Linear(attn_dim, attn_dim)
        self.key = torch.nn.Linear(attn_dim, attn_dim)
        self.value = torch.nn.Linear(attn_dim, attn_dim)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor):

        query = self.query(query)  # Compute the dot product of the query and key
        key = self.key(key)
 
        query = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it

        attn_mask = torch.full((query.size(-3), query.size(-2)), float('-inf')).to(query.device)
        attn_mask = attn_mask.masked_fill_(torch.eye(query.size(-3)).bool(), 0.0)
        
        attn_weight = torch.softmax(query + attn_mask, dim=-1).float()
 
        output = (attn_weight @ self.value(key)).float()
        return output


# Initializing the model
m  = Attention(512)
 
# Inputs to the model
query   = torch.randn(64, 8, 512) # The shape of query is [batch_size, sequence length, embedding dimension]
key     = torch.randn(64, 8, 512) 

__output__  = m(query, key)

