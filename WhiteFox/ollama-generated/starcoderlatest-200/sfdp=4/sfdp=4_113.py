
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.ones(1, 3, 64, 64)
 
    def forward(self, qk, value):
        attn_weight = torch.softmax((qk @ key.transpose(-2, -1)) / math.sqrt(qk.size(-1)), dim=-1)
        output = attn_weight @ value
        return output


# Inputs to the model
qk = torch.randn(8, 3, 64, 64)
value = torch.randn(8, 3, 64, 64)
