
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 256)
        self.key = torch.nn.Linear(3, 256)
        self.value = torch.nn.Linear(3, 256)
 
    def forward(self, x1):
        vq = self.query(x1).unsqueeze(-1)
        vk = self.key(x1).unsqueeze(-2)
        v = self.value(x1).unsqueeze(0)
        qk = torch.cat((vq, vk), dim=-1)  # Q * K
        attn_mask = (qk / math.sqrt(vq.size(-1))).unsqueeze(-1)  # [B, QK] / sqrt([QK])
        qk = qk + attn_mask  # [B, QK+1]
        attn_weight = torch.softmax(qk, dim=-1)  # [B, QK] / softmax([QK])
        v  = attn_weight @ v  # [B, QK] @ V
        return v


# Initializing the model
m = Model()


