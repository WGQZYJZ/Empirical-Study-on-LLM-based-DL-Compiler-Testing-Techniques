
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.attn  = torch.nn.Linear(512, 512)
 
    def forward(self, x1, attn_mask):
        v1  = self.conv(x1)
        qk  = v1 @ self.attn.weight.transpose(-2, -1) / math.sqrt(v1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output  = attn_weight @ v1
        return output


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
attn_mask = torch.ones(1, 512).byte()
__output__  = m(x1, attn_mask)


