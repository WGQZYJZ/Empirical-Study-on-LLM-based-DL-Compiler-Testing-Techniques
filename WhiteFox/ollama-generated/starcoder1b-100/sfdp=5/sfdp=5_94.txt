
class Model(torch.nn.Module):
    def __init__(self, hidden_size=8, heads=16):
        super().__init__()
        self.linear = torch.nn.Linear(hidden_size * 4, 512)
        self.layernorm = torch.nn.LayerNorm(512)

    def forward(self, x):
        query = self.linear(x[:, :, :hidden_size])
        key = self.linear(x[:, :, hidden_size:2 * hidden_size])
        value = self.linear(x[:, :, 2 * hidden_size:])

        query = self.layernorm(query)
        key = self.layernorm(key)
        value = self.layernorm(value)
        query = torch.cat([query, query], dim=-1)
        key = torch.cat([key, key], dim=-1)
        output = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key

        attn_weights = torch.softmax(output, dim=-1)  # Apply softmax to the result

        output = torch.dropout(attn_weights @ value, dropout_p, True)
        return output


# Initializing the model
m = Model()


