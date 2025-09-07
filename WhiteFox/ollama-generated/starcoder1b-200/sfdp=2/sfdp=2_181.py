
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(4096, 2048)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        q_scale = qk.div(inv_scale_factor)
        k_scale = qk.div(inv_scale_factor)
 
        attn  = self.attn(q_scale)
        attn  = torch.nn.functional.dropout(attn, p=dropout_p)
        v     = self.attn(k_scale)
        v_scale = v.div(v.norm(dim=-1, keepdim=True).clamp_min_(1e-3))
 
        return attn * (value / v_scale)


# Initializing the model
m = Model()
