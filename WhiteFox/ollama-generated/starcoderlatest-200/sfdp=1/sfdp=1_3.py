
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, mask=None):
        qk  = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk  = qk / np.sqrt(key.size(-1))
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = self.attn_layer.dropout_module_(softmax_qk)

        output = torch.matmul(dropout_qk, value) 
        return output


# Initializing the model
m = Model()
query = torch.randn(3, 64, 512).to('cuda')
key = torch.randn(3, 64, 512).to('cuda')
value = torch.randn(3, 64, 512).to('cuda')
mask = torch.rand(1, 1, query.shape[-2], key.shape[-2]).to('cuda')
