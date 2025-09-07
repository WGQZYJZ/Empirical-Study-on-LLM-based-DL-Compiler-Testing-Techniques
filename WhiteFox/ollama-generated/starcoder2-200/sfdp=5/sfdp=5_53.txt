
class Model(torch.nn.Module):
    def __init__(self, attn_mask=None, dropout_p=0.1):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(64, 8)
        self.dropout = torch.nn.Dropout(dropout_p)
 
    def forward(self, query, key, value):
        vq  = self.attn(query=query, key=key, value=value)[0]
        return self.dropout(vq)


# Initializing the model
m1 = Model()


# Inputs to the model
qk  = torch.randn(32, 64, 64) # Query of size [batchsize x seq_len x 64]
key  = torch.randn(32, 64, 64) # Key of size [batchsize x seq_len x 64]
value  = torch.randn(32, 64, 8) # Value of size [batchsize x seq_len x 8]


__output__1  = m1(qk, key=key, value=value)[0]