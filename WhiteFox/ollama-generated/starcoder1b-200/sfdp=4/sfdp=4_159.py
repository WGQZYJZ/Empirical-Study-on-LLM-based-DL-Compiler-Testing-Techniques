
class Model(torch.nn.Module):
    def __init__(self, hidden_size, num_heads):
        super().__init__()
        self.hidden_size  = hidden_size
        self.num_heads    = num_heads
 
        self.query = torch.nn.Linear(hidden_size * 2, hidden_size)
        self.key   = torch.nn.Linear(hidden_size * 2, hidden_size)
        self.value = torch.nn.Linear(hidden_size, hidden_size)
 
    def forward(self, x1, x2):
        q = self.query(torch.cat((x1, x2), dim=1))  # Compute the query tensor for two sequences
        k = self.key(torch.cat((x1, x2), dim=1))   # Compute the key tensor for two sequences
        v = self.value(torch.cat((x1, x2), dim=1)) # Compute the value tensor for two sequences
        dot  = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        attn_weights  = torch.softmax(dot, dim=-1)    # Apply softmax to the result
        output        = (attn_weights * v).sum(dim=0)  # Compute the weighted sum of the value tensor
        return output


# Initializing the model
m = Model()


