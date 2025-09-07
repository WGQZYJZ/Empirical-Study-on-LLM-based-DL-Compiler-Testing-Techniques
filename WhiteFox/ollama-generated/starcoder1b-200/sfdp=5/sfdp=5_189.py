
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 5)
        self.key = torch.nn.Linear(12, 7)
        self.value = torch.nn.Linear(8, 6)
 
    def forward(self, query_data):
        v = torch.cat([
            query_data,
            query_data,
            query_data,
            query_data
        ], dim=-1).reshape(-1, 5)
        k = self.key(query_data)
        q = self.query(query_data)
        w1 = torch.bmm(q, k.transpose(-2, -1)) / math.sqrt(k.size(-1))
        w2 = torch.bmm(w1, v) / math.sqrt(w1.size(-1))
        return w2


# Initializing the model
m  = Model()

