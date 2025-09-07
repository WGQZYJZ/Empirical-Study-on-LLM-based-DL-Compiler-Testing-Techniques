
class Model(torch.nn.Module):
    def __init__(self, d_model, num_heads=8):
        super().__init__()
        self.d_model = d_model
        self.num_heads = num_heads
 
        self.qkv = torch.nn.Linear(d_model, 3 * d_model)
        self.attn = torch.nn.Softmax(dim=-1)
        self.v = torch.nn.Linear(d_model, d_model)
 
    def forward(self, x1):
        query = self.qkv(x1).chunk(2, dim=0)  # (batch size, num heads, length, depth)
        query = [torch.cat((q[:, :, i : i + 1], q[:, :, i + 1 :]), dim=-1) for i in range(self.num_heads)]  # (batch size, length, 2 * d_model)
        key   = self.qkv(x1).chunk(2, dim=0)
        value = self.v(x1)
        out   = [torch.cat((query[i], key[i]), dim=-1) for i in range(self.num_heads)]
        return [self.attn(*out[i]) for i in range(self.num_heads)]


# Initializing the model
m = Model(d_model=64, num_heads=8)
m.eval()


