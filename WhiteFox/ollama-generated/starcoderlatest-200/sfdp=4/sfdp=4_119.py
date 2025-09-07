
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, query, key, value, attn_mask=None):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask if attn_mask is not None else qk # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 4, 256, 256)
key   = torch.randn(1, 4, 256, 256)
value = torch.randn(1, 4, 256, 256)
attn_mask = torch.ones((1, 2, 256, 256)) # This is a self-attention mask which prevents attention to certain positions


# Expected output of the model
__expected__ = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask if attn_mask is not None else query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))


# The following example checks the model prediction and expected output match
assert TorchScriptTest(m, (query, key, value, attn_mask)).check()

