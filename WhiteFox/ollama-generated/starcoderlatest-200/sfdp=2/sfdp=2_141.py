
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2, mask):
        qk  = self.attention(x1, x2, x2, mask=mask)
        output = self.attention(qk[0], qk[1], qk[2], key_padding_mask=qk[3])
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 8, 64, 64)
x2 = torch.randn(20, 12, 64, 64)
mask = x1 != 0
