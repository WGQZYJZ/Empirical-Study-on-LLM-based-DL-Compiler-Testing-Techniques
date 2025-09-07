
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(dim, dim*3)
 
    def forward(self, x1, x2):
        k1, v1, qk  = torch.split(self.qkv(x2), [dim, dim, dim * 3], -1)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v1)

        # Calculate the output of the self-attention layer
        output  = output * 0.5
        output  = output + x1
 
        # Calculate the output of the cross-attention layer
        v2  = self.qkv(x1)
        k2, v2, qk2 = torch.split(v2, [dim, dim, dim*3], -1)
        scaled_qk2 = qk2.div(inv_scale_factor)
        softmax_qk2 = scaled_qk2.softmax(dim=-1)
        dropout_qk2 = torch.nn.functional.dropout(softmax_qk2, p=dropout_p)
        output2 = dropout_qk2.matmul(v2)
 
        # Calculate the output of the cross-attention layer
        output2  = output2 * 0.5
        output2  = output2 + x1
 
        return output, output2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, dim, N)
x2 = torch.randn(1, dim, M)
__output__, __output2__ = m(x1, x2)
 
