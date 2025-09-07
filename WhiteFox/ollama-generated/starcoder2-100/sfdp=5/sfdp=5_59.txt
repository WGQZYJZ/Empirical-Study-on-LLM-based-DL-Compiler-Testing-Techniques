
class Model(torch.nn.Module):
    def __init__(self, num_heads=1024, key_size = 65 * 3, value_size = 64):
        super().__init__()
        
        self.key   = torch.randn((num_heads//8, 127, int(key_size/8), int(value_size / 8)))
        self.value = torch.randn((num_heads // 8, 30, 4))

    def forward(self, query):
        v2   = key @ query.transpose(-2, -1)  # Compute the dot product of the key and query
        v3   = qk + attn_mask  # Add the attention mask to the scaled dot product
        v4   = torch.softmax(v3, dim=-1)  # Apply softmax to the result
        v5   = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        v6   = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return v4 * v2


# Initializing the model
m = Model()


# Inputs to the model<|end_of_input|>
x1  = torch.randn(3, 65)
