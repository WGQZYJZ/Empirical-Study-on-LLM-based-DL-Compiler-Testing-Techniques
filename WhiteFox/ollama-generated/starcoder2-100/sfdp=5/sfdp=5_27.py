
class Model(torch.nn.Module):
    def __init__(self,
                 attn_dropout=0.,
                 residual_dropout=0.,):
        super().__init__()
 
        self.attn = torch.nn.MultiheadAttention(64, 8)
        self.dropout1 = torch.nn.Dropout(residual_dropout)
 
    def forward(self, x1):
        v1 = None
        v2 = self.dropout1(v1)
 
        v3 = self.attn(v1)[0]
        v4 = v3 + v1  # Add 1 to the output of the error function
        v5 = v2 * v4
        return v5


# Initializing the model