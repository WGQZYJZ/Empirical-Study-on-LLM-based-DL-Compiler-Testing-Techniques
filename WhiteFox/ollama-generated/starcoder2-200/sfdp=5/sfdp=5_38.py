
class MultiHeadedAttention(torch.nn.Module):
    def __init__(self, hidden=512, n_head=8):
        super().__init__()
        self.hidden = hidden

        self.n_head  = n_head
 
        self.q_proj = torch.nn.Linear(hidden, hidden)
        self.k_proj = torch.nn.Linear(hidden, hidden)
        self.v_proj = torch.nn.Linear(hidden, hidden)
 
        self.out   = torch.nn.Linear(hidden, hidden)
 
    def forward(self, query):
        q  = self.q_proj(query)
        k  = self.k_proj(query)
        v  = self.v_proj(query)

        # Compute the dot product of the query and key, and scale it
 
        scaled_dot = torch.einsum("...nq, ...nk -> ...qn", q, k / math.sqrt(self.hidden))
 
        attn_mask  = torch.full((q.shape[1], k.shape[1]), -float('inf'), dtype=torch.float32)
        masked = torch.triu(attn_mask).masked_fill_(attn_mask >0, float('-inf'))
        # Add the attention mask to the scaled dot product

        qk  = scaled_dot + masked
 
        # Apply softmax to the result
 
        attn_weight  = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
 
        # Compute the dot product of the dropout output and the value

        out = attn_weight @ v
 
        # Apply a linear layer to the result
        
        final  = self.out(out)
        return final

# Initializing the model
m1 = MultiHeadedAttention()

# Inputs to the model
query  = torch.randn(32, 512).to(device)

__output__  = m1(query)

