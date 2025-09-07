
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(3, 8)
        self.key   = torch.nn.Linear(3, 8)
        self.value = torch.nn.Linear(8, 16)

    def forward(self, query, key, value):
        qk = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        attn_mask = torch.zeros((key.size(-1),), device=value.device) # The attention mask for a linear layer is 0
        attn_mask[:, value.view(-1).long()] = 1 # The attention mask is set to 1 at the positions where the key and values are not equal
        attn_weights = torch.softmax(qk, dim=-1) * attn_mask # Compute the attention weights using softmax
        output = (attn_weights @ value).view(-1, 16) # Apply the dot product of the weights and the values
        return output


# Initializing the model
m = Model()
