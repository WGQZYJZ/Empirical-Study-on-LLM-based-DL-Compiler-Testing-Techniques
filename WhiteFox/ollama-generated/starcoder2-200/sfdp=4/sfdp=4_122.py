
class TransformerModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
 
    def forward(self, x1, x2, x3):
        v1  = (x1 + x2 * x3) / math.sqrt(x1.size(-1))
        v2  = v1 + x2 
        v3  = self.linear(v2)
        return v3


# Initializing the model
m  = TransformerModel()
 
# Inputs to the model
x1 = torch.randn(40, 512) # The size of batch is 40; the number of hidden units is 512.
x2 = torch.randn(38, 64) # The size of batch is 38 and each sequence length is 64
x3 = x2 / math.sqrt(x1.size(-1)) # The size of the third input tensor is equal to that of v2 after using the square root.
__output__= m(x1, x2, x3)

