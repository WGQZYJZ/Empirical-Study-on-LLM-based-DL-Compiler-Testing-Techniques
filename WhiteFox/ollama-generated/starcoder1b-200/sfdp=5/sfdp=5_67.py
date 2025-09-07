
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(20, 5)
        self.key   = torch.nn.Linear(16, 4)
        self.value = torch.nn.Linear(13, 8)
 
    def forward(self, x):
        query_v = self.query(x)
        key    = self.key(x)
        value   = self.value(x)
        scale  = math.sqrt(value.size(-1)) / math.sqrt(query_v.size(-1))
        scaled = torch.div(query_v, scale)
        v      = scaled @ value
        return v


# Initializing the model
m = Model()

