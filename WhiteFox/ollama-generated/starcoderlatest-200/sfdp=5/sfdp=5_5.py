
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64 * 2, 32)
        self.key = torch.nn.Linear(64 * 2, 32)
 
    def forward(self, x1):
        qk = torch.matmul(x1.transpose(-2, -1), self.query).contiguous() + self.atten_mask.unsqueeze(0).to(device)
        attn_weight = F.softmax(qk / math.sqrt(qk.size(-1)), dim=-1)
        output = torch.matmul(attn_weight, x1).contiguous()
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
