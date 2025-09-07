
class MultiheadAttention(torch.nn.Module):
    def __init__(self, n_heads=8):
        super().__init__()
        self.n_heads = n_heads
        self.linear_query  = torch.nn.Linear(32, 1)
        self.linear_key   = torch.nn.Linear(32, 1)
        self.linear_value  = torch.nn.Linear(32, 80)
 
    def forward(self, query): 
        # Query
        q = self.linear_query(query).permute([0, 2, 1])
 
        # Key
        k = self.linear_key(q).transpose(-2, -1)
 
        # Value
        v = self.linear_value(q).transpose(-2, -1)
 
        # Compute the dot product of the query and key
        attn_mask = torch.triu(torch.ones([k.size(-2), k.size(-1)]), diagonal=0)  # Attention mask 
        attn_mask = attn_mask.masked_fill_(attn_mask, -float("inf"))  # Mask the attention weights
        attn_weights = torch.softmax(q @ k / math.sqrt(query.size(-1)), dim=-2)  # Softmax on the dot product of query and key
        output = v * attn_weights
 
        return output


# Initializing the model
m = MultiheadAttention()


# Inputs to the model
x1  = torch.randn([3,80])

# Model inference

__output__  = m(x1)
