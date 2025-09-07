
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.head = torch.nn.Linear(embed_dim, embed_dim) # Linear layer with embedding dimension as the input and output dimensions respectively
        self.key  = torch.nn.Linear(embed_dim, embed_dim)
        self.value= torch.nn.Linear(embed_dim, embed_dim)

    def forward(self, x1):
        n, e, m, _ = x1.size()

        # [n * h, (e/h), m] -> [(e/h), n * h, m] -> [[e], n * h, m]
        v1 = self.head(x1).view([n, -1, e])
        # [n * h, (e/h)] -> [e, n * h] -> [1, 2736, 105]
        k1 = self.key(v1).view(-1, e) 
        # [(e/h), m] -> [m, n * h] -> [105, n * h] -> [[n], e, m]
        v2 = self.value(v1).view([e, -1])
        attn_mask = torch.triu(torch.ones((1, 2736))).byte() # Triangular mask for the attention mask

        # [1, 2736, e] @ [[n], e, m] -> [[n], (m), e]
        v3 = torch.bmm(attn_mask.unsqueeze(0).expand([n, -1, m]), v2)
        
        # Softmax the result of scaled dot-product attention 
        qk  = k1 @ v3.transpose(-2, -1) / math.sqrt(v3.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output  = attn_weight @ v2 # Compute the dot product of the attention weights and the value

        return output
# Initializing the model
m = MultiHeadAttention()
# Inputs to the model
x1 = torch.randn(3, 64, 768)
