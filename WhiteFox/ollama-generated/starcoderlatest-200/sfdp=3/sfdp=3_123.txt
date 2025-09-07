
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 8)
 
    def forward(self, q, k, v):
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) # compute the dot product of the query and key tensors
        softmax_qk = scaled_qk / math.sqrt(k.size(-1)) # softmax the result of the dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)  # apply dropout to the softmax output
        output = dropout_qk @ v  # compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(1, 3, 64, 64)
k = torch.randn(1, 8, 64, 64)
v = torch.randn(1, 8, 64, 64)
