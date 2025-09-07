
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_mask = torch.zeros([qk.shape[0], qk.shape[-2]], dtype=qk.dtype, device=qk.device)
        output = self._masked_softmax(qk, mask=attn_mask) @ value  # Compute the dot product of the dropout output and the value
        return output
 
    def _masked_softmax(self, x, mask):
        with torch.no_grad():
            m_exp = (x * mask.unsqueeze(-1).type(x.dtype)) - 1e6 * (1 - mask.unsqueeze(-1).type(x.dtype))
        return F.softmax(m_exp.masked_fill(mask==0, -1e6), dim=-1)

# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
