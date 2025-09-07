
class TransformerModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.transformer = nn.TransformerEncoderLayer(d_model=512, nhead=8)
 
    def forward(self, x1):
        attn_mask  = torch.ones(x1.shape).masked_fill_(torch.tril(torch.zeros(*x1.shape)) == -float("inf"), float("-inf"))
 
        # Input to the model is the query tensor
        v1  = self.transformer(query=x1, key=x1, value=x1) + attn_mask
 
# Initializing the model
m  = TransformerModel()


# Inputs to the model
x1  = torch.randn(80, 5296).masked_fill_(torch.tril(torch.zeros(*x1.shape)) == -float("inf"), float("-inf"))
__output__  = m(x1)

