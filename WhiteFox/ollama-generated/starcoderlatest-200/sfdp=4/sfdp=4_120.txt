
class Attention(torch.nn.Module):
    def __init__(self, n_query, n_key, n_value):
        super().__init__()
        self.query = torch.nn.Linear(n_query, n_key) # A linear layer that receives the query tensor as an input and outputs a tensor whose size is (batch, key_length, query_dimension)
        self.key = torch.nn.Linear(n_key, n_value) # A linear layer that receives the key tensor as an input and outputs a tensor whose size is (batch, query_length, value_dimension)
    
    def forward(self, x1, x2):
        qk  = self.query(x1) @ self.key(x2).transpose(-2, -1) / math.sqrt(x2.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Attention(32, 64, 128)


# Inputs to the model
x1 = torch.randn(1, 32, 128)
x2 = torch.randn(1, 64, 32)
