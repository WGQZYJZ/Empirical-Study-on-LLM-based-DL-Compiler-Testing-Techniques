
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(16, 8)
        self.key = torch.nn.Linear(16, 8)
        self.value = torch.nn.Linear(16, 8)
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.query.weight) / math.sqrt(x1.size(-1))
        attn_mask = torch.zeros_like(qk).scatter(dim=-2, index=torch.LongTensor([[0, 0]]), value=float('-inf'))
        output = torch.matmul(attn_mask + qk, self.value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 16, 256, 256)
