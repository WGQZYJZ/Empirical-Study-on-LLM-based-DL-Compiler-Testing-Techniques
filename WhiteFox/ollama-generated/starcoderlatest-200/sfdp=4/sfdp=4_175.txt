
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.nn.Parameter(torch.ones((1, 64, 64)))
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + self.attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(2, 64, 1) # (batch_size, num_head, len_q, len_kv), where batch_size can be 2 or 3 and num_head is fixed at 64
key  = torch.randn(8, 64, 1) # The shape of key is same as query in this example
value  = torch.randn(8, 64, 1)
