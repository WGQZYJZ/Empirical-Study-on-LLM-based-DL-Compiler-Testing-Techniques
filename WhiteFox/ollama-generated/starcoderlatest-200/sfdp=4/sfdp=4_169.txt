
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 128)
        self.key = torch.nn.Linear(64, 128)
 
    def forward(self, query, key):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model and initializing the inputs to the model
m = Model()
attn_mask = torch.randn(16, 32).unsqueeze(-1).unsqueeze(-2) * -1e10
x1 = torch.randn(8, 32, 512, 512)


# Generating the output
