
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.query = torch.nn.Parameter(torch.Tensor(1, 3, 64, 64))
        self.key   = torch.nn.Parameter(torch.Tensor(1, 3, 64, 64))
 
    def forward(self, x1):
        qk = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.key.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        value   = self.conv(x1).contiguous().view(1, 8, -1) * attn_weight.view(-1, 1, 1, 1) # Scale the dot product by the attention weights
        return value


# Initializing the model
m = Model()


