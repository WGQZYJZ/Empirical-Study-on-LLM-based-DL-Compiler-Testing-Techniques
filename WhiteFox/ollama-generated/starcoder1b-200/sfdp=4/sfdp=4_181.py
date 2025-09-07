
class Model(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
        self.w_proj = torch.nn.Linear(d_model, d_model)
        self.k_proj = torch.nn.Linear(d_model, d_model)
        self.v_proj = torch.nn.Linear(d_model, d_model)

    def forward(self, query, key, value):
        w1 = F.softmax(self.w_proj(query), dim=-1)  # softmax of dot-product of input queries and keys
        k1 = F.softmax(self.k_proj(key), dim=-1)
        v1 = self.v_proj(value)  # value projection
        return torch.matmul(w1, k1) @ v1


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(3, 64, 64)
key = torch.randn(3, 64, 64)
value = torch.randn(3, 64, 64)
