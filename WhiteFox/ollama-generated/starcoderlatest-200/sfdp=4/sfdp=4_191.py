
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_proj = torch.nn.Linear(192, 128)
        self.ff_proj = torch.nn.Sequential(
            torch.nn.Linear(128, 128), 
            torch.nn.ReLU()
        )
        self.self_attn_layer_norm = torch.nn.LayerNorm([192, 128])
 
    def forward(self, query, key, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
 
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        output = output.transpose(-2, -1).reshape(output.size(0), output.size(-2), -1)
        
        x = self.attn_proj(output) # Apply linear projection to generate attention logits
        logits = self.ff_proj(x)  # Apply linear projection and ReLU

        return logits


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 192, 64, 64)
key = torch.randn(8, 192, 64, 64)
attn_mask = torch.randn(1, 8, 64, 64)
