
class SelfAttention(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.embed = torch.nn.Linear(embed_dim, 1024)
        self.out = torch.nn.Linear(1024 + embed_dim, 1024)
 
    def forward(self, input_ids=None, attention_mask=None):
        query = self.embed(input_ids).transpose(-2, -1) / math.sqrt(query.size(-1))
        key = query 
        qk = query @ key.transpose(-2, -1)  # Scaled dot product attn 
        qk += attention_mask
 
        attn_weight = torch.softmax(qk, dim=-1)
        value = self.out(input_ids).transpose(-2,-1) * attn_weight  # Weighted sum of values using the attention weights.
        return value


# Initializing the model
model = SelfAttention(embed_dim=50)
 
