
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.randn(128, 4096)
        self.key = torch.randn(3 * 512,)
        self.value = torch.randn(768, 3, 512)
 
    def forward(self):
        qk = torch.einsum('ij, ij->i', (self.query, self.key)) / math.sqrt(
            self.query.size(-1))
 
        attn_mask = torch.zeros([768] + [3 * 512], dtype=torch.float)
        attn_mask += torch.triu(attn_mask, diagonal=-769).to(device=torch.device("cuda"))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk / math.sqrt(1024), dim=-1)
        output = (attn_weight @ self.value).permute([2, 3, 0, 1])
 
        return output

# Initializing the model
m = Model()
 
# Inputs to the model
