
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(64, 10)
 
    def forward(self, x2, x3):
        v7, v8  = self.att(x2, x3, attn_mask=None, key_padding_mask=None) 
        return v7
 
# Initializing the model
m  = Model()

 # Inputs to the model
x2  = torch.randn(10, 64, 5, 5)
x3  = torch.randn(10, 64, 5, 5)
__output__  = m(x2, x3)

