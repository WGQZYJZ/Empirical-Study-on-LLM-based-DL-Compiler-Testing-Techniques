
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.attn = Attention()
 
    def forward(self, query, key, value, attn_mask):
        v1 = self.qkv_1(query)
        qk  = v1 @ torch.transpose(key, -2, -1) / math.sqrt(v1.size(-1)) + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
x3 = torch.randn(1, 8, 64, 64)
x4 = torch.randn(1, 64, 64)

 # Model output
