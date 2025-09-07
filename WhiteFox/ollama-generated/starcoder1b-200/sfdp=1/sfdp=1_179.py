
class Model(torch.nn.Module):
    def __init__(self, n_head=8, dim=16):
        super().__init__()
        self.query = torch.nn.Linear(dim, dim)
        self.key = torch.nn.Linear(dim, dim)
        self.value = torch.nn.Linear(dim, dim)
        self.attn = torch.nn.Linear(2 * dim, n_head)
 
    def forward(self, x1):
        # Compute the dot product of query and key tensors
        qk = self.query(x1)  # [B, Lq, Lk]
        k = self.key(x1)  # [B, Lk, D]
        v = self.value(x1)  # [B, Lv, D]
        # Scale the dot product by an inverse scale factor and apply softmax to compute scaled dot product [B, Lq, H]
        qk_softmax = qk.div(self.scale).softmax(-2)  # [B, Lq, H]
        dropout_qk = torch.nn.functional.dropout(qk_softmax, p=dropout_p)  # Apply dropout to softmax output [B, Lq, H]
        scaled_value = v.mul_(self.scale).unsqueeze(-2)  # [B, Lv, D], [B, Lv, D, 1]
        scaled_value += dropout_qk.matmul(x1.permute(0, 2, 1))  # Compute the dot product of the dropout output and value tensor [B, H, Lv]
        attn = self.attn(scaled_value)  # [B, Lq, H], [B, Lq, H, D]
        # Apply softmax to scaled dot product and compute dropout [B, H, Lq]
        out = attn.softmax(-2)  # [B, H, Lq]
        return out


# Initializing the model
m = Model()
x1 = torch.randn(1, 64, 64, 3)
