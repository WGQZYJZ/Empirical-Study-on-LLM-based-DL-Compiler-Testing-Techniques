
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Conv2d(16, 4, 5, stride=2, padding=0)
 
    def forward(self, x1):
        qk = torch.einsum('ncxhwxd->ncyhxwd', (self.q(x1), x1)) / math.sqrt(4 * 384)
        attn_weight = softmax(qk, dim=-1)
        output = attn_weight @ v
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
