
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer  = torch.nn.Linear(768, 384)
 
    def forward(self, x1, x2):
        q1 = x1.view(-1, 512) # Linearly project the query and key to the same dimensions
        k1 = x2.transpose(-2, -1).contiguous().view(-1, 512) 
        v1 = self.attn_layer(torch.cat((q1, k1), dim=-1)) 
        attn_weight  = torch.softmax(v1 * math.sqrt(v1.size(-1)), dim=-1)
        return torch.matmul(attn_weight, x2).view(x1.shape[0], -1, 8, 64, 64)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 512, 64, 64)
x2 = torch.randn(1, 3, 768, 64, 64)
