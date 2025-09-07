
class Model(torch.nn.Module):
    def __init__(self, qkv):
        super().__init__()
        self.qkv = torch.nn.Linear(d_model, d_k)
        self.dense = torch.nn.Linear(d_k, 2*n_head)

    def forward(self, x1, x2):
        k, v = self.qkv(x1).chunk(2, dim=-1)  # Split the query and key
        q = torch.cat([torch.sin(k), torch.cos(k)], dim=-1)  # Compute sin(q), cos(q) with kernel size 2
        attn = (q @ v).softmax(-1)  # Softmax to compute attention weights, then dropout for numerical stability
        v *= attn  # Scale dot product of scaled query and value
        output = x2 @ v.transpose(-1, -2)  # Dot product of scaled value and key-value matrices
        return output


# Initializing the model
model = Model(qk_v)

