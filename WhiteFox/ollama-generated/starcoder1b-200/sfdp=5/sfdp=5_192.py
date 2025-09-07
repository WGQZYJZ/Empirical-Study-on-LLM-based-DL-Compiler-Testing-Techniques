
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key   = torch.nn.Linear(4, 4)
        self.value = torch.nn.Linear(4, 8)

    def forward(self, x1, x2):
        query = self.query(x1)
        key   = self.key(x2)
        value = self.value(x1)

        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk += attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value

        return output


# Initializing the model
m = Model()


