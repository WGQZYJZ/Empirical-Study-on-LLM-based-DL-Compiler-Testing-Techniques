
class Model(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.embed_dim = embed_dim
        self.proj1 = torch.nn.Linear(2 * self.embed_dim, 512) 
        self.proj2 = torch.nn.Linear(512, 8 * embed_dim)
 
    def forward(self, query, key):
        x = torch.cat([query, key], dim=1)
        # Residual connection + linear layer: [batch, len, emb_dim] -> [batch, len, emb_dim] 
        v = F.relu(self.proj1(x))
        output = self.proj2(v).permute(0, 2, 1)
        return output


# Initializing the model
m = Model(8)

# Inputs to the model
query = torch.randn(1, 3, 64, 64) # [batch, len, emb_dim]
key = torch.randn(1, 8, 64, 64)  # [batch, head_num * num_head, seq_len, dim_per_head]
