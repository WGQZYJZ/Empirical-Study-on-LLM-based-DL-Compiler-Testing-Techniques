
class MultiHeadAttentionModel(torch.nn.Module):
    def __init__(self, qk_dim=160, v_dim=48):
        super().__init__()
 
        self.query  = torch.nn.Linear(qk_dim, qk_dim)
        self.key  = torch.nn.Linear(v_dim, qk_dim)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor):
        # Compute dot product of queries and keys (plus an attention mask) 
        qk = self.query(query) @ self.key(key).transpose(-2, -1) / math.sqrt(self.key.out_features)
 
        # Add the attention mask to the scaled dot product
        attn_mask  = torch.full((qk.shape[-2], kq.shape[-1]), -np.inf)
        attn_mask[torch.arange(qk.shape[-1])[:, None] < torch.arange(qk.shape[-1])[None, :]]  = np.NINF
 
        # Compute softmax over the keys and apply dropout to the attention weights
        attn_weight = torch.softmax(qk + attn_mask, dim=-1) 
        attn_weight = torch.dropout(attn_weight, p=0.15, training=self.training)

        # Compute output by computing dot product of attention weight and values
        output  = attn_weight @ key
 
        return output

# Initializing the model
m  = MultiHeadAttentionModel()

# Inputs to the model:
v  = torch.randn(64, 250) # Input vector
q1  = torch.randn(80, 3) # Query vector 1
q2  = torch.randn(70, 3) # Query vector 2

