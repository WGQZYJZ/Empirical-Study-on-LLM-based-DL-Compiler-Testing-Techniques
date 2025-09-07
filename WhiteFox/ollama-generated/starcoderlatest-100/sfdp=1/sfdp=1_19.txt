
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(num_heads=4, embed_dim=16)
 
    def forward(self, query, key, value):
        scaled_qk = self.attn(query, key, value)[0]
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(2048, 64, 1, 1) # N x C x W x H
key    = torch.randn(2048, 32, 56, 56) # N x C' x W/s x H/s
value  = torch.randn(2048, 32, 128, 128) # N x C' x W x H
