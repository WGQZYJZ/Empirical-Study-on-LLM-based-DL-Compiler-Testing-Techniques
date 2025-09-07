
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 512)
        self.key = torch.nn.Linear(128, 512)
        self.value = torch.nn.Linear(128, 512)
 
    def forward(self, x):
        q = F.normalize(self.query(x), dim=-1)
        k = F.normalize(self.key(x), dim=-1)
        v = F.normalize(self.value(x), dim=-1)
        #qk = torch.bmm(q, k.transpose(-2, -1)) / math.sqrt(q.size(-1))
        attn_mask  = torch.arange(x.shape[0]).view(1,-1).expand(-1, -1024) != (torch.arange(1, x.shape[0] + 1).view(-1, -1)).view(-1, 1).transpose(0, 1)
        attn_mask = attn_mask.to(dtype=x.dtype).to(device=x.device)
        qk = torch.einsum('bdn,bdm->bnd', (q, k)) / math.sqrt(q.shape[-1]) + attn_mask
        attn_weight  = torch.softmax(qk, dim=-1)
        output = torch.einsum('bnd,bdm->bdn', (attn_weight, v))
        return output


# Inputs to the model
x1 = torch.randn(20, 64, 7, 7)
