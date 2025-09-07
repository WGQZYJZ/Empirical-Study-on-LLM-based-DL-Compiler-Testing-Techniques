
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_layer = torch.nn.Linear(768, 1024)
        self.key_layer = torch.nn.Linear(768, 1024)

    def forward(self, x1, attn_mask):
        qk = self.attention_query(@x1, @x1) # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk + attn_mask, dim=-1) # Apply softmax to the result
        output = @attn_weight * @x2 # Compute the dot product of the attention weights and the value

        return output
