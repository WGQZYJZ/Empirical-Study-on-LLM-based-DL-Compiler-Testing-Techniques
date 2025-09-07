
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        return 0


# Inputs to the model
query  = torch.randn(2, 64, 128)
key    = torch.randn(2, 64, 128)
value  = torch.randn(2, 64, 32)
