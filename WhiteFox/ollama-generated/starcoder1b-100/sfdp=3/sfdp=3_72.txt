
class Model(torch.nn.Module):
    def __init__(self, num_queries, num_keys, dprate):
        super().__init__()

        self.query = torch.nn.Linear(num_queries, dprate * 2)
        self.key   = torch.nn.Linear(num_keys,     dprate * 2)
        self.scale = nn.Parameter(torch.ones(1))

    def forward(self, x):
        query = self.query(x).unsqueeze(1)
        key   = self.key(x)

        v = torch.matmul(query, key.transpose(-2, -1))
        k = v / math.sqrt(float(dprate * 2))
        k *= (scale_factor - 1)
        v = torch.nn.functional.softmax(k, dim=-1)
        v = dropout(v, p=self.p)

        # The value is now `v` and the result is `dropout * softmax` and `v * scale`.

        value = torch.matmul(v, x).unsqueeze(-1)

        return value

# Initializing the model
m = Model(num_queries=64, num_keys=32, dprate=0.5)

# Inputs to the model
x = torch.randn(1, 64, 64)
