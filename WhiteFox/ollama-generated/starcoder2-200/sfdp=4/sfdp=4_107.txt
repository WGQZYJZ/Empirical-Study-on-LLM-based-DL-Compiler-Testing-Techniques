
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dropout=0.1):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout)
 
    def forward(self, query, key, value, attn_mask):
        attn_query  = (
            torch.softmax(
                query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)), dim=-1))  # Compute the dot product of the query and key tensors
        attn_query += attn_mask # Add the attention mask to the scaled dot product
        attn = self.dropout(torch.softmax(attn_query, -1)) # Apply softmax to the result
        return (
            torch.einsum('...ij,...jk->...ik', attn, value)  # Compute the dot product of the attention weights and the value tensor
        )

class MultiHeadAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
        self.query = torch.nn.Linear(config['d_model'], config['d_k']) # Create a linear layer for computing the query tensor
        self.key = <KEY>(config['d_model'], config['d_k']) # Create a linear layer for computing the key tensor
        self.value = torch.nn.Linear(config['d_model'], config['d_v']) # Create a linear layer for computing the value tensor
 
        self.attn = ScaledDotProductAttention()
 
    def forward(self, query, key, value):
 
        attn_mask = torch.zeros((query.size(-2), key.size(-1))).to(query)  # Initialize an attention mask to zeros
        attn_mask = attn_mask.masked_fill(attn_mask == 0, float('-inf'))  # Set the entries in the attention mask that correspond to invalid positions to -∞
 
        query  = self.query(query) 
        key  = self.key(key)
        value  = self.value(value)
 
        return self.attn(
            query, 
            key, 
            value, 
            attn_mask
        )

class TransformerModel(torch.nn.Module):
    def __init__(self, config: dict):

        super().__init__()
 
        self.layers = [MultiHeadAttention(config)] * (len(config['layers'])) # Initialize a stack of MultiHeadAttention modules
        self.model_dim = config['d_model']
 
    def forward(self, query):
        # Define the initial hidden state and add it to every layer
        hidden  = query * math.sqrt(self.model_dim)
 
        for layer in self.layers:
            hidden = layer(query, hidden, hidden)
 
        return hidden

# Initializing the model
config  = {
  'd_k':  64, 
  'd_v':  32, 
  'd_model':   1000, 
  'layers': [
      {
          'd_model': 768, 
          'head_dim':  64
      }
  ]
}
t  = TransformerModel(config)

