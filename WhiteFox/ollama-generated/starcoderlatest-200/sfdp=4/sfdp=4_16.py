
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(8, 16)
        self.key = torch.nn.Linear(32, 40)
 
    def forward(self, x1, x2):
        q1 = self.query(x1)
        k1 = self.key(x2)
        attn_mask = (k1 == -1).unsqueeze(1)
        qk1 = torch.matmul(q1, k1.transpose(-2, -1)) / math.sqrt(x1.size(-1)) + attn_mask
        attn_weight = torch.softmax(qk1, dim=-1)
        output = torch.matmul(attn_weight, x2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8)
x2 = torch.randn(5, 32)
