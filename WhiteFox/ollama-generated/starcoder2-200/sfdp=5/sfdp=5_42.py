
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn(512)
        self.key = <KEY>(4096, 512)
        self.value = torch.randn(4096, 512)
 
    def forward(self, attn_mask):
        vq = self.query @ self.key.transpose(-2, -1) / math.sqrt(
            self.query.size(-1))
        vv = vq + attn_mask
        wv = torch.softmax(vv, dim=-1)
        return wv @ self.value


# Initializing the model
m  = Model()

# Input to the model
attn_mask  = 0.5 * (1 - torch.triu(torch.ones(4096, 4096), diagonal=1)) / math.sqrt(512)

