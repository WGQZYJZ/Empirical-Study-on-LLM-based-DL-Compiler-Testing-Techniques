
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(1024, 64)
 
    def forward(self, q, k, v):
        # Compute the dot product of the query and the key
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        # Compute the dot product of the dropout output and a value
        output = dropout_qk.matmul(v)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(128, 3, 160, 160) # query tensor (batch size x embed dim x input sequence length x feature map depth)
k = torch.randn(128, 3, 96, 96) # key tensor (batch size x embed dim x output sequence length x feature map depth)
v = torch.randn(128, 3, 140, 140) # value tensor (batch size x embed dim x output sequence length x feature map depth)
