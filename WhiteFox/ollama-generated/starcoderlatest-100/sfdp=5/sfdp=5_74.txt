
class Model(torch.nn.Module):
    def __init__(self, query_size, embed_dim, num_heads):
        super().__init__()
        self.query = torch.nn.Linear(query_size, embed_dim)
        self.key   = torch.nn.Linear(query_size, embed_dim)
        self.value = torch.nn.Linear(query_size, embed_dim)
 
    def forward(self, query, key, value):
        attn  = torch.matmul(query, self.query.weight.t())
        # Compute the dot product of the query and key, and scale it
        # Scale by sqrt(k.size(-1)), since keys are queries here
        attn *= 0.5 / (self.key.out_features ** 0.5)
        # Add the attention mask to the scaled dot product
        attn += torch.einsum('b n d, b n e -> b n d e', [attn_mask, self.key(key)])
        attn = torch.softmax(attn, dim=-1).masked_fill_(~attn_mask, -float('inf'))
        # Apply softmax to the result
        attn = torch.dropout(attn, dropout_p)  # apply dropout to attention weights
        output = attn @ self.value(value)  # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model(query_size=10, embed_dim=256, num_heads=8)

