
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.query(x1)
        v2 = self.key(x2)
 
        attn_weights = (v1 @ v2.transpose(-2, -1)) / math.sqrt(v1.size(-1))
        attn_weights += torch.eye(attn_weights.shape[-2], device=attn_weights.device).type(torch.bool).unsqueeze(0)
        
        output = torch.matmul(attn_weights, x2).permute(0, 3, 1, 2) * (v1 @ v2.transpose(-2, -1)).reciprocal()
        return output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
