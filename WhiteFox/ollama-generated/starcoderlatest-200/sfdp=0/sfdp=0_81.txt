
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = ScaledDotProductAttention()
 
    def forward(self, x1, x2):
        # Query tensor: Batch size x 768
        q = torch.matmul(x1, x2.transpose(-1, -2))
        # Key tensor: Batch size x 512
        k = torch.einsum('nc,vw->nw', (x1, x2))
        # Value tensor: Batch size x 512
        v = torch.einsum('nc,vw->nw', (x1, x2))
 
        y = self.attention(q, k, v)
        return y
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(3, 768) # Batch size x hidden_size
x2 = torch.randn(3, 512) # Batch size x hidden_size
