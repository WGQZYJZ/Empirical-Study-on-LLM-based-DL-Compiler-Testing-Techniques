class MultiHeadedAttentionModel(torch.nn.Module):
    def __init__(self, h, d):
        super().__init__()

        self._d = d  # the dimensionality of keys, values and queries (equal to embedding_dim)
        self._h = h  # the number of heads

        # Wq,Wk,Wv,Wo are three fully connected layers used in attention. 
        # All weights are initialized as 1/sqrt(d), d is the size of embedding dimensionality
        self.Wq = torch.nn.Linear(self._d, self._d)
        self.Wk = torch.nn.Linear(self._d, self._d)
        self.Wv = torch.nn.Linear(self._d, self._d)

        # output is the concatenation of all heads
        self.Wo = torch.nn.Linear(h*d , d)

    def forward(self, query, key):
        
