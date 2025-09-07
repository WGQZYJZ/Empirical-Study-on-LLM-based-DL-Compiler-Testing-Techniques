
class Model(torch.nn.Module):
    def __init__(self, attn_dropout=0):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention()
        self.dropout  = nn.Dropout2d(attn_dropout)
 
    def forward(self, x1, x2):
        v1, v2  = self.attn(x1, x2, x1) # compute the attn weights for inputs v1 and v2
        return self.dropout(v2)


# Initializing the model
m = Model()
x1 = torch.randn(3, 4, 64, 64)
