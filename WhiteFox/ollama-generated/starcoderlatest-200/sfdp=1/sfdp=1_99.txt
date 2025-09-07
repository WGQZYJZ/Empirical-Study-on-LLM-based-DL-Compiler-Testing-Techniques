
class Attention(torch.nn.Module):
    def __init__(self, kdim=128, vdim=64):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(kdim, vdim)
 
    def forward(self, q_in, k_in, v_in):
        q, k, v = q_in, k_in, v_in
 
        q, k, v = self.attn(q, k, v)
        return q


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn1 = Attention()
 
    def forward(self, x1, k_in, v_in):
        attn 1 output tensor
 
        query, key, value = torch.split(attn1 output tensor, [x1.size(0), -1, -1], dim=0)

        return query
# Inputs to the model
x1 = torch.randn(3, 128, 64, 64)
k_in = torch.randn(3, x1.size(-2), x1.size(-1))
v_in = torch.randn(3, x1.size(-2), x1.size(-1))
