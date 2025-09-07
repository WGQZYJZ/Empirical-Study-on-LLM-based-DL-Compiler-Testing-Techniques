
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_weight = torch.nn.Softmax(dim=-1)
 
    def forward(self, query, key, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        att = self.attention_weight(qk).transpose(-2, -3) @ value
        return output


# Initializing the model
m = Model()

