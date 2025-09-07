
class AttentionModule(torch.nn.Module):
    def __init__(self, input_dim=256, query_dim=1024):
        super().__init__()
        self.layer = torch.nn.Sequential(
            torch.nn.Linear(input_dim, query_dim), 
            torch.nn.Tanh(), 
        )

    def forward(self, x):
        return self.layer(x)

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = AttentionModule() # The query module
        self.k = AttentionModule() # The key module

    def forward(self, q, k):
        v1  = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1)) + mask # Compute the dot product of the query and key, and scale it by root(query_dim), plus an attention mask to the scaled dot product
        v3  = torch.softmax(v2, dim=-1) 
        v4  = self._dropout(v3) 
        return v4 @ k

# Initializing the model