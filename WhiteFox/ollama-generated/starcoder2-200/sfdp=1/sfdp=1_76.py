class Attention(torch.nn.Module):
    def __init__(self, d_model=768, nhead=12, dropout=0.1):
        super().__init__()
 
        self.d_model = 768 
        self.nhead = 12
        self.dropout = 0.1
         
        self.inv_scale_factor = (self.d_model ** -0.5)
        self.softmax = torch.nn.Softmax(dim=-1)
 
        # This is the model for the query, key, and value tensors.
        self.key = torch.nn.Linear(768, 32 * nhead)
        self.query = torch.nn.Linear(768, 32 * nhead)
        self.value = torch.nn.Linear(768, 32 * nhead)
 
    def forward(self, x):
 
        # Computes the dot product of the query and key tensors.
        k = self.key(x).view(-1, 32*nhead, 32*nhead)
        q = self.query(x).view(-1, 32 * nhead, 32 * nhead)

        v = self.value(x)
        # Scales the dot product by an inverse scale factor.
        scaled_qk = q @ k.transpose(-2,-1) / (self.dmodel ** -0.5) 
        # Computes the softmax for the scaled dot product.
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p, training=self.training) 
        # Computed the dot product of the dropout output and the value tensor.
        v  = dropout_qk @ v
        return v
m = Attention()
