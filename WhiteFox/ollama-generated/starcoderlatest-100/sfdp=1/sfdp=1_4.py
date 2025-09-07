
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, dim=1024, heads=8, dropout_p=0.1):
        super().__init__()
 
        # Add self-attention layer
        self.attention = torch.nn.Linear(dim, dim * 3)
 
        # Use the same number of attention heads and multiplying factor to produce query tensor for each head
        self.qkv = torch.nn.Linear(dim, dim * heads * 3, bias=False)
 
        # Add linear projections in case of using different values on different positions in decoder layers
        self.out_proj = torch.nn.Linear(dim * 2 * heads, dim)
        
        self.dropout1 = torch.nn.Dropout(p=dropout_p)
        self.dropout2 = torch.nn.Dropout(p=dropout_p)
        
    def forward(self, x):
        # Shape: (batch_size, seq_length, hidden_dim)
        bsz, sl = x.shape[:2]
 
        qkv_output  = self.qkv(x).chunk(3, dim=-1)
        
        # Query tensor has the shape of (batch_size * num_heads, seq_length, hidden_dim_per_head)
        q, k, v = qkv_output[:bsz], qkv_output[bsz:2*bsz], qkv_output[2*bsz:]
 
        # Shape: (batch_size * num_heads, sl, sl) 
        qk = torch.matmul(q, k.transpose(-2, -1))
 
        # Shape: (batch_size * num_heads, sl, sl)
        scale = math.sqrt(float(self.attention.in_features) / (float(self.attention.out_features) // self.attention.groups))
        qk = qk.div(scale).unsqueeze(-2)
 
        # Shape: (batch_size * num_heads, sl, sl)
        attention_probs = torch.nn.functional.softmax(qk, dim=-1)
        attention_probs = self.dropout1(attention_probs)
        attn_output  = torch.matmul(attention_probs, v)
 
        # Shape: (batch_size * num_heads, sl, hidden_dim_per_head) 
        attn_output = attn_output.transpose(1,2).contiguous().view(bsz, -1, self.attention.out_features)
 
        # Add projection and combine with input
        x = torch.cat([attn_output, x], dim=-1)
        
        out = self.dropout2(self.out_proj(x))

        return out


# Initializing the model
m = MultiHeadAttention()


# Inputs to the model
bsz = 8
sl = 64
x = torch.randn(bsz, sl, 1024)
