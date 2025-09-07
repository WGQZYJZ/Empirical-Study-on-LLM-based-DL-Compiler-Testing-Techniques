
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 20) 
        self.key = torch.nn.Linear(10, 20)
        self.value = torch.nn.Linear(10, 20)
 
    def forward(self, query, key, value):
        # Perform the dot product between the queries and keys (query @ key.transpose(-2, -1)) 
        attn_weights = torch.einsum('...t,...s->...ts', query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        # Add the attention mask to the scaled dot product (attn_weights + 1)
        attn_weights += 1
        # Apply softmax on the result
        attn_weights = torch.softmax(attn_weights, dim=-1)
        # Perform dropout operation with a probability of p (attn_weights * dropout)
        output = attn_weights @ value
        return output
 
# Initializing the model
m = Model()


class KeyValueDataset:
    