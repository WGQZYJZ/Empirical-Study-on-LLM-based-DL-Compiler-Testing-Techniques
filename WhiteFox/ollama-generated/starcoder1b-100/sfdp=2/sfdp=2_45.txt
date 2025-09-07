
class Model(torch.nn.Module):
    def __init__(self, embedding_dim):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, embedding_dim)

    def forward(self, x1, x2, attention=True):
        query  = self.embedding(x1)
        key    = self.embedding(x2)
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(self.embedding_dim)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)

        v  = self.embedding(x2) * math.sqrt(self.embedding_dim)
        dropout_v = torch.nn.functional.dropout(v, p=dropout_p)

        if attention:
            output = dropout_qk.matmul(dropout_v) # Compute the dot product of the dropout output and the value
        else:
            output = dropout_qk * dropout_v # Compute the dot product of the dropout output and the value
        return output


# Inputs to the model
x1, x2 = torch.randn(1, 3, 64, 64), torch.randn(1, 5, 64, 64)
