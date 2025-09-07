
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 10) # 256 -> 10
        self.key = torch.nn.Linear(256, 10)   # 256 -> 10
        self.value = torch.nn.Linear(256, 10) # 256 -> 10
 
    def forward(self, qk, attn_mask):
        attn_weight = torch.softmax(qk + attn_mask, dim=-1) # Compute the attention weights
        output = attn_weight @ self.value # Compute the dot product of the attention weights and the value tensor
        return output
