
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_proj = torch.nn.Linear(64, 64*3)

    def forward(self, x1, x2):
        v1 = self.qkv_proj(x1).chunk(3, dim=-1)
        qk, value = v1[:2], v1[2]

        attn_weight = torch.softmax((qk@key.transpose(-2, -1))/math.sqrt(query.size(-1)), dim=-1)  # Compute the dot product of the query and key, and scale it
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value

        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64)  # Shape [B, C, T_q]
x2 = torch.randn(2, 3, 64)  # Shape [B, C, T_k]


