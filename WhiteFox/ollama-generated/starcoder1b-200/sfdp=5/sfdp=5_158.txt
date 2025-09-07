
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 128) # Query vector
        self.key   = torch.nn.Linear(768, 128) # Key vector
        self.value = torch.nn.Linear(128, 128) # Value vector

        self.dropout = nn.Dropout(0.5)

    def forward(self, query, key):
        assert query.size() == (batch_size, seq_length, input_dim)
        assert key.size() == (batch_size, seq_length, input_dim)

        # Compute the dot product of the query and key, and scale it
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        qk = self.dropout(qk)

        attn_weights = nn.Softmax()(qk)
        out = torch.matmul(attn_weights, value) # Compute the dot product of the dropout output and the value
        return out

# Initializing the model
m  = Model()

