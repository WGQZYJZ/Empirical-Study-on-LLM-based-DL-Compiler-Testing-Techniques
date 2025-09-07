
class Model(torch.nn.Module):
    def __init__(self, dim_query, dim_key, dim_value, dim_model):
        super().__init__()
        self.dim_query = dim_query  # Dimension of the query (i.e., hidden state)
        self.dim_key   = dim_key    # Dimension of the key (i.e., word embedding)
        self.dim_value = dim_value  # Dimension of the value (i.e., target or context)
        self.dim_model = dim_model  # Dimension of the model (i.e., output size)
 
        self.query  = torch.nn.Linear(dim_query, dim_model // 2)
        self.key    = torch.nn.Linear(dim_key,   dim_model // 2)
        self.value  = torch.nn.Linear(dim_value, dim_model)
 
    def forward(self, q, k):
        # Reshape query and key into tensors of shape [batch_size, seq_len, embed]
        b, seq_len, _ = q.shape
 
        hq, hc  = self.query(q).chunk(2, dim=-1)  # Query and key as (B, H, embed)
        hk, hk  = self.key(k).chunk(2, dim=-1)  # Reshape keys into [batch_size, seq_len, dim_model // 2]
 
        # Compute the scaled dot product with mask for numerical stability.
        attn = torch.einsum('bij,bik->bi', hc, hk) + 0.1 * (torch.eye(seq_len, device=hc.device)[None] - hc).unsqueeze(-2).expand_as(attn)
 
        # Apply dropout to the attention weights
        attn = torch.dropout(attn, dropout_p, True)
 
        # Compute model output
        h  = torch.einsum('bij,bi->b', attn, hc)  # Reshape results back into (B, seq_len, dim_model)
        h  = h.contiguous().view(b, -1, self.dim_model)  # Reshape model output to [B * T, H]
 
        # Project model output to (seq_len, embed)
        return self.value(h)


# Initializing the model
m = Model(dim_query=2048, dim_key=1024, dim_value=256, dim_model=512)


# Inputs to the model
x1 = torch.randn(1, 3, 2048, 1024)
y1 = torch.randn(1, 3, 1024, 256)
