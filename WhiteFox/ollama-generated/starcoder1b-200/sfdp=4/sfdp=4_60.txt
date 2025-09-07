
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        v3 = self.conv(x3)
 
        qk = (v1 * v2).transpose(-2, -1) / torch.sqrt(v1.size(-1))
        attn_mask = torch.ones((qk.shape[:-2]), dtype=torch.float).triu(diagonal=1)  # Get the triangular attention mask
        
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ v3
 
        return output


# Initializing the model
m = Model()
