
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(2, 3)
        self.key = torch.nn.Linear(2, 3)
 
    def forward(self, query, key):
        attn_weight = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) + \
                     1e-9 * torch.ones_like(attn_weight)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(1, 2, 3)
key = torch.randn(1, 2, 3)
