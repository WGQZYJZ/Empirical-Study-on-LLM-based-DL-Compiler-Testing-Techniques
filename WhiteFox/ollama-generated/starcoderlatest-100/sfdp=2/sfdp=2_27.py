
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(dim, dim)

    def forward(self, query, key):
        v1 = query @ key.transpose(-2, -1)
        v2 = v1 / scale_factor
        v3 = torch.softmax(v2, dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        v5 = self.qk(v4).matmul(value)
        return v5


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(16, dim)
key = torch.randn(16, dim)
