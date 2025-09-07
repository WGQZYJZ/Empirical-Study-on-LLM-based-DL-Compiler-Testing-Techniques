
class Attention(torch.nn.Module):
    def __init__(self, dim_keys, dim_values, dim_attention, p=0., qk=False):
        super().__init__()
        if qk:
            self.q = torch.nn.Linear(dim_queries, dim_attention)
            self.k = torch.nn.Linear(dim_keys, dim_attention)
        else:
            self.proj = torch.nn.Linear(dim_queries, dim_attention)

        if qk:
            self.v  = torch.nn.Linear(dim_values, dim_attention)

    def forward(self, x):
        if qk:
            proj1 = self.q(x)
            proj2 = self.k(x)

            attn = torch.bmm(proj2, proj1.transpose(-2, -1)) # Dot product between queries and keys
            attn = attn / np.sqrt(dim_attention ** 0.5)
        else:
            proj = self.proj(x)
            attn = torch.matmul(proj, proj.transpose(-2, -1))

        return attn

    def _init_(self):
