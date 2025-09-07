
class Model(torch.nn.Module):
    def __init__(self, query, key, value):
        super().__init__()
        self.query = torch.nn.Linear(32, 16)
        self.key = torch.nn.Linear(32, 16)
        self.value = torch.nn.Linear(32, 8)
        self.attn_mask = torch.randn(4096, 4096).gt_(5.).float()

    def forward(self):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk += attn_mask 
        attn_weight  = torch.softmax(qk, dim=-1)  
        output = self.value @ attn_weight # Compute the dot product of the dropout output and the value
        return output

m = Model()


__output__  = m()
