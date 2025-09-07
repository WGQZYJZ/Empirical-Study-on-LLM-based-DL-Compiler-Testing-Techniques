
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(256, 3 * 3)
 
    def forward(self, x1, x2):
        q1 = self.qkv(x1).view(-1, 3, 3)
        k1 = self.qkv(x2).view(-1, 3, 3)
 
        v1 = torch.cat((v1, k1, q1), dim=0)  # Merge key and query with the values to compute attention weights
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        return torch.matmul(attn_weight, v1).view(-1, v1.size(-2), v1.size(-3))
 
 