
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2):
        v  = self.attn(x1, x2, x2)[0]  # Compute the attention weights from the query and key tensors
        return v
