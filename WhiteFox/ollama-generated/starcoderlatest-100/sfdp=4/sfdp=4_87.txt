
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_weight = torch.nn.Parameter(torch.randn(8, 16))
 
    def forward(self, query, key, value):
        attn_weights = (query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))).softmax(dim=-1) + 1e-5
        output = attn_weights @ value
        return output


# Initializing the model
m = Model()
q = torch.randn(16, 32, 64, 64).cuda()
k = torch.randn(8, 16, 128, 128).cuda()
v = torch.randn(32, 8, 128, 128).cuda()


# Inputs to the model
