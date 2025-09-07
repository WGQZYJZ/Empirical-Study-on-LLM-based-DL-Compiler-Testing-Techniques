
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.size(-1))
        v1 += 0

        return v1


# Initializing the model
m = SelfAttention()

# Inputs to the model
q1 = torch.randn(1, 8, 3, 64)
k2 = torch.randn(1, 3, 64, 64)
v2 = torch.randn(1, 8, 64, 64)
