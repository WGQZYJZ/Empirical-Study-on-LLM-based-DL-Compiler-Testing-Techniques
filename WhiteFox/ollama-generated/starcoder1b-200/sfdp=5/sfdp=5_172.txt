
class Model(torch.nn.Module):
    def __init__(self, dim_q=512, dim_k=64, dim_v=64, dim_o=8):
        super().__init__()
        self.query = torch.nn.Linear(dim_q, dim_k)  # Query layer
        self.key    = torch.nn.Linear(dim_k, dim_k)  # Key layer
        self.value  = torch.nn.Linear(dim_v, dim_v)  # Value layer
        self.out_proj = torch.nn.Linear(dim_v, dim_o)  # Output layer

    def forward(self, x1):
        qk = torch.matmul(x1, self.query) / math.sqrt(self.key.size(-1))
        attn_mask = (torch.eye(qk.size(-2), kq.size(-1)) - torch.pow(attn_p, 2))
        attn_weight = torch.softmax(qk * attn_mask, dim=-1)
        value = self.value * attn_weight
        output = torch.matmul(output, attn_weight)
        output = output + x1
        return self.out_proj(output)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
