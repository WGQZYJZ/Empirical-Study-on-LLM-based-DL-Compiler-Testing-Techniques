
class Model(torch.nn.Module):
    def __init__(self, embedding_dim: int = 256, heads: int = 4, head_dim: int = 64):
        super().__init__()
        self.embed_queries = torch.nn.Linear(input_dim, heads * head_dim)
        self.q_transform = torch.nn.Sequential(torch.nn.Linear(heads * head_dim, embedding_dim),
                                             torch.nn.ReLU(),
                                             torch.nn.Linear(embedding_dim, heads * head_dim))

    def forward(self, x):
        q  = self.embed_queries(x)
        qk = q.view(-1, self.heads, self.head_dim).transpose(-2, -1)
        k  = self.q_transform(qk).contiguous().view(-1, self.heads, self.heads * self.head_dim)

        return qk, k

    @property
    def heads(self):
        return int(self.q_transform[-1].in_features / self.q_transform[0].out_features)


# Inputs to the model
x = torch.randn(16, 32, 32)
qk, k = m(x) # The type of qk and k should be <torch.FloatTensor>

