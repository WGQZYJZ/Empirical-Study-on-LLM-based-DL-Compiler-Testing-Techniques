
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Embedding(vocab_size, hidden_size)
        self.key    = torch.nn.Embedding(vocab_size, hidden_size)
        self.value  = torch.nn.Embedding(vocab_size, hidden_size)
        self.scale  = 1. / (10 ** (0.5 * hidden_size))
 
    def forward(self, x):
        # Get the embedding vectors of the words in the input tensor
        query = self.query(x[:, :hidden_size])
        key   = self.key(x[:, hidden_size:])
 
        v = torch.matmul(query, key.transpose(-2, -1))
        v = v / (self.scale * torch.sqrt(torch.sum((v ** 2), dim=-1).clamp(min=0)))
        softmax = F.softmax(v, dim=-1)
        dropout = F.dropout(softmax, p=dropout_p)
        output = torch.matmul(dropout, self.value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(2, 3, 50, 50)
