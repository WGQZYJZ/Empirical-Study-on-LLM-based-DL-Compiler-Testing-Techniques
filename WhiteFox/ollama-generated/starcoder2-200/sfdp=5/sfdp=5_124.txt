
class AttnModel(torch.nn.Module):
    def __init__(self, attn_dropout=0.1):
        super().__init__()
        self.attn  = torch.nn.Linear(32 * 5, 64) # Initialize the weight matrix of the attention mechanism 
        self.drop  = torch.nn.Dropout(attn_dropout)
 
    def forward(self, query, key, value, attn_mask):
        kq_score  = (query @ key.transpose(-2, -1)) / math.sqrt(key.size(-1)) # Compute the dot product of the query and key 
        kq_score += attn_mask
        attn_weight  = torch.softmax(kq_score, dim=-1) # Apply softmax to the scaled dot product 
        attn_weight  = self.drop(attn_weight) # Apply dropout on the output of the softmax operation
        out  = (attn_weight @ value) # Compute the dot product of these attention weights and the value 
        return out


# Initializing the model
model1  = AttnModel()

# Inputs to the model
query, key, value, attn_mask  = torch.randn(32, 5), torch.randn(32, 64 * 5), torch.randn(32, 64 * 5), torch.randn(32, 10)

