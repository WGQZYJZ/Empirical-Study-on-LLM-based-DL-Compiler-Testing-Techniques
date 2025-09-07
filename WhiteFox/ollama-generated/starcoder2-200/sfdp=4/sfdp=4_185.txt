
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 768)
        self.key = torch.nn.Linear(128, 512)
        self.value = torch.nn.Linear(3072, 4096)
 
    def forward(self, input_tensor):
        v1  = self.query(input_tensor)
        v2  = self.key(input_tensor)
        v3  = v1 @ v2.transpose(-2, -1) / math.sqrt(v1.size(-1))
        v4  = v3 + attn_mask 
        v5  = torch.softmax(v4, dim=-1)
        