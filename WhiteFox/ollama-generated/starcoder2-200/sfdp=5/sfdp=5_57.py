
class Attention(torch.nn.Module):
    def __init__(self, query, key, value, mask=None, pdrop=0.1):
        super().__init__()
        self.query = torch.nn.Linear(query[-1], 8)
        self.key = torch.nn.Linear(key[-1], 8)
        self.value = torch.nn.Linear(value[-1], 8)
 
        # Use the mask to block the attention weights on the masked positions.
        self.attn_mask = mask
 
        # The dropout layer is not a part of the standard transformer encoder block;
        # it is added for demo purposes in this notebook.
        self.dropout = torch.nn.Dropout(pdrop)
 
    def forward(self, x):
        q = self.query(x)  # Compute the query
        k = self.key(x) + self.attn_mask  # Add the attention mask to the key
        v = self.value(x)
 
        qk = torch.softmax((q @ k.transpose(-2, -1)) / math.sqrt(query[-1]),
                           dim=-1)  # Compute softmax on scaled dot product of query and key
        attn_output = (self.dropout(qk) * v).sum(dim=0)
 
        return attn_output

# Initializing the model
attn_model = Attention(query, key, value)

