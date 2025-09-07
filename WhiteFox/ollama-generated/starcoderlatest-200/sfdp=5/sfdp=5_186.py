
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_norm = torch.nn.LayerNorm([32, 64])
        self.query = torch.nn.Linear(128, 32)
        self.key = torch.nn.Linear(128, 32)
        self.value = torch.nn.Linear(128, 32)
 
    def forward(self, query, key, value):
        attn_input = torch.cat((query, key), dim=0).transpose(-1, -2) # Concatenate the values of the keys and queries in the last two dimensions
        attn_output = torch.matmul(attn_input, self.key.weight.t())
        attn_mask = torch.zeros(attn_output.size()).scatter_(-1, key.unsqueeze(0), 1) # Create a soft attention mask
        attn_weight = torch.softmax(attn_output + attn_mask * -1e36, dim=-2) # Apply softmax to the scaled dot product of the query and key (plus an attention mask), followed by a dropout operation
        output = torch.matmul(attn_weight, self.value.weight) # Compute the dot product of the dropout output and the value
        attn_output = self.attn_norm(attn_input + torch.matmul(attn_weight, value)) # Compute the attention output of the attention mechanism
        return attn_output
 
# Inputs to the model (batch size 2)
query = torch.randn(128, 32, 64, 64)
key = torch.randn(64, 128, 64, 64)
value = torch.randn(64, 128, 64, 64)
