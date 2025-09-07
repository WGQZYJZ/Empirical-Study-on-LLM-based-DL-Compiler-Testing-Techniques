
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(16, 32) # Linear layer for query vector
        self.key = torch.nn.Linear(16, 32) # Linear layer for key vector
        self.value = torch.nn.Linear(16, 32) # Linear layer for value vector
 
    def forward(self, query, key): 
        # Compute the dot product between the query and key vectors (query @ key.transpose(-2,-1))
        qk = self.query(query).matmul(self.key(key).transpose(-2, -1)) / math.sqrt(self.config.dim)

        # Mask out invalid positions
        attn_mask = (key != 0).unsqueeze(1).expand(-1, qk.size(1), -1)
        attn_mask = attn_mask.float()
        output = torch.where((attn_mask == False) & (qk >= 0), qk.softmax(dim=-1), qk) # Softmax and attention
        return output
# Inputs to the model
m = Attention()
query = torch.randn(3, 64)
key = torch.randn(64, 32)
