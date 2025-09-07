
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 512)
        self.key = torch.nn.Linear(64, 512)
        self.value = torch.nn.Linear(32, 512)
 
    def forward(self, q, k):
        attn_score = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(q.size(-1))
        attn_mask = (attn_score > 0).type(torch.float)
        v = torch.matmul(attn_weight, value)
        return output
 
# Initializing the model
m = Model()

