
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 3)

    def forward(self, query, key, value, mask=None):
        v = query @ key.transpose(-2, -1) / math.sqrt(key.size(-1)) # Compute the dot product of the query and key tensors, and scale them by sqrt(hidden_dim)
        if mask is not None:
            attn_mask = torch.zeros_like(v).type(torch.ByteTensor)  # (batch_size, hidden_size)
            attn_mask = attn_mask.masked_fill_(mask == 1, float('-inf')) # Set the attention mask to zero for padded positions
        else:
            attn_mask = None
        attn_weight = torch.softmax(v, dim=-1) # Apply softmax on the result of the dot product
        output = attn_weight @ value # Compute the weighted sum of the values

        return output


# Initializing the model
m  = Model()


# Inputs to the model
q = torch.randn(10, 768)
k = torch.randn(2, 768)
v = torch.randn(2, 384)
