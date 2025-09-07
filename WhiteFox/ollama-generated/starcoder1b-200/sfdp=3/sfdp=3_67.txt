
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Embedding(n_words, d_k)
        self.key = torch.nn.Embedding(n_words, d_k)
        self.value = torch.nn.Parameter(torch.Tensor(1))
 
    def forward(self, x):
        x = self.query(x)  # Query with shape (batch size, query dimension)
        x = self.key(x)  # Key with shape (batch size, key dimension)
        value = self.value
        return x + value


# Initializing the model
m = Model()

