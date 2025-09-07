
class Model(torch.nn.Module):
    def __init__(self,
                 dim=768,
                 num_heads=12,
                 hidden_dim=3072,
                 dropout=None):
        super().__init__()
 
        self.query = torch.nn.Linear(hidden_dim, 2 * dim)
        self.key = torch.nn.Linear(hidden_dim, 2 * dim)
        self.value = torch.nn.Linear(hidden_dim, 48)
        self.scale = math.sqrt(torch.tensor([3072]).float())  # The scaling factor
        self.norm1 = torch.nn.LayerNorm(normalized_shape=[self.scale])
        self.norm2 = torch.nn.LayerNorm(normalized_shape=[hidden_dim, dim * num_heads])
 
        self.attn_mask = torch.ones([48, 3072], dtype=torch.bool).to(device="cuda")  # The attention mask
        self.dropout1 = torch.nn.Dropout(p=dropout)
        self.dropout2 = torch.nn.Dropout(p=dropout)
 
    def forward(self, hidden_states):
        query  = self.query(hidden_states).view([-1, num_heads]).permute([0, 2, 1])
        key  = self.key(hidden_states).view([-1, num_heads]).permute([0, 2, 1])
 
        v  = query @ key / math.sqrt(query.size(-1)) # Compute the dot product of the query and key (divide by square root of the number of heads)
        v  += self.attn_mask  # Add the attention mask to the scaled dot product
        v  = torch.softmax(v, dim=-2)   # Apply softmax to the result
        v  = self.dropout1(v)  # Apply dropout to the softmax output
 
        attn_out  = v @ hidden_states.permute([0, 2, 1]) / math.sqrt(hidden_states.size(-1))   # Compute the dot product of the dropout output and the hidden states
        attn_out = self.norm1(attn_out)
 
        out  = self.dropout2(attn_out @ self.value.permute([0, 2, 1])) * scale / math.sqrt(self.scale)   # Compute the dot product of these attention weights and the value
        out  = self.norm2(out).view([-1, dim])
 
        return out

# Initializing the model
m  = Model()

