
class AttentionModule(torch.nn.Module):
    def __init__(self, dim_q, dim_k, dim_v):
        super().__init__()
        self.dim_q = dim_q # dimension of query space
        self.dim_k = dim_k  # dimension of key space
        self.dim_v = dim_v  # dimension of value space
 
    def forward(self, query, key, attn_mask):
        qk = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1))  # scaled dot product
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)  # softmax attention weights
        output = attn_weight @ value  # weighted sum of the values for each head
        return output
# Initializing the model
m = AttentionModule(dim_q=32, dim_k=64, dim_v=80)


# Inputs to the model
query  = torch.randn(1, 80, 512, 896) # dimension of query space
key    = torch.randn(1, 64, 896, 256) # dimension of key space
attn_mask = torch.randn(1, 64, 512, 896).bool() # attention mask


