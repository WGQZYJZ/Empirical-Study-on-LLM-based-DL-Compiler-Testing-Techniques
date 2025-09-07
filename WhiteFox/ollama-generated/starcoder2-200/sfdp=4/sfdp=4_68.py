
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(30, 64)
        self.key = torch.nn.Linear(30, 128)
        self.value = torch.nn.Linear(30, 128)
 
    def forward(self, x):
        vq  = self.query(x).unsqueeze(-2)
        vk  = self.key(x).transpose(-2, -1) / math.sqrt(64)
        attn_mask  = torch.zeros_like(vk[..., :30]) + float("-inf")
        attn_mask[attn_mask == 0] = -torch.finfo('float').max
        vqk  = (vq @ vk).masked_fill(attn_mask, -1e9)
        weights = torch.softmax(vqk, dim=-1)
        return vqk  @ self.value(x), weights


# Initializing the model
m  = Model()


# Inputs to the model
x = torch.randn(30, 32, dtype=torch.float64)


