
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 5)
 
    def forward(self, q, k, v, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask # Compute the scaled dot product of the query and key, and then add the attention mask to it
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output
# Initializing the model
m = Model()

