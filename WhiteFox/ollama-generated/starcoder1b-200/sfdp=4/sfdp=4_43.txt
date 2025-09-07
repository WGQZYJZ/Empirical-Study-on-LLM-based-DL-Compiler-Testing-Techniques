
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 3)
        self.key   = torch.nn.Linear(10, 6)
        self.value = torch.nn.Linear(20, 4)
 
    def forward(self, x1):
        qk = self.query(x1).matmul(self.key.transpose(-2, -1)) / math.sqrt(x1.size(-1))
        qk  = qk + (1 - attn_mask)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()


# Inputs to the model
input = torch.randn(4, 10)
key   = torch.randn(3, 6)
query = torch.randn(3, 20)
