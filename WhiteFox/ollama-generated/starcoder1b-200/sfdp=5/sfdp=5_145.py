
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(768, 32)
        self.layer_norm1 = nn.LayerNorm(32)
        self.layer_norm2 = nn.LayerNorm(32)
 
    def forward(self, x):
        query = self.qkv(x).chunk(3, dim=-1) # Split the input tensor into three chunks of three tensors: batch_size, hidden_size, depth
        attn_weights  = query[0] @ query[1].transpose(-2, -1) / math.sqrt(query[0].size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weights  = nn.functional.softmax(attn_weights, dim=-1)  # Apply softmax to the result
        output = attn_weights @ query[2] # Compute the dot product of the dropout output and the value
        x = self.layer_norm1(x + output)
        x = F.gelu(x)
        x = self.layer_norm2(x + output)
        return x


# Initializing the model
m = Model()
