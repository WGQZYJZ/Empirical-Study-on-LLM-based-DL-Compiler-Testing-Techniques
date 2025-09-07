
class Model(torch.nn.Module):
    def __init__(self, num_keys=1024, num_values=3072, attn_heads=8, dropout_p=0.2):
        super().__init__()
        self.num_keys  = num_keys
        self.num_values = num_values
        self.attn_heads = attn_heads
        self.dropout_p = dropout_p

        self.query = torch.nn.Linear(self.num_keys, self.num_keys)
        self.key    = torch.nn.Linear(self.num_keys, self.num_keys)
        self.value  = torch.nn.Linear(self.num_values, self.num_keys)

        self.softmax = nn.Softmax(dim=-1)

    def forward(self, query, key, value):
        # Reshape the queries and keys
        batch, seq_len = query.size()[:2]
        shape     = (batch * attn_heads, -1)
        query     = query.view(*shape, self.num_keys)
        key       = key.view(*shape, self.num_keys)
        value     = value.view(*shape, self.num_keys)

        # Compute the attention weights
        # The dot product of query and key is defined as: qk @ (qk' / math.sqrt(query.size(-1)))^2
        # We need to use torch.bmm(q, k, transb=False), which calculates matrix multiplication only on the positive diagonal, i.e., it does not change the input size when the matrices are transposed.
        # So we just reverse the input so that: q' = query, k' = key. The dot product is calculated as torch.bmm(query, key).t() * torch.bmm(key, key)
        attn_weight  = torch.bmm(query.t(), key) / math.sqrt(query.size(-1))
        attn_weight  = torch.dropout(attn_weight, self.dropout_p, True)

        # Apply the attention weights to the values, which is the output of the dropout operation
        value = self.softmax(torch.bmm(value, attn_weight)) * key.size(-1)**-0.5  # Multiply by sqrt(d_k), and scale back into (query, key) space

        return value


# Initializing the model
m = Model()

