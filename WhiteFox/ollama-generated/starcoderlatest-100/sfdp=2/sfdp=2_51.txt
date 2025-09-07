
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1)) * 0.5
        softmax_qk = (v1 / math.sqrt(key.shape[-1])).softmax(dim=-1)
        v2 = dropout(softmax_qk, p=dropout_p).matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(4096, 128)
key   = torch.randn(4096, 128)
value = torch.randn(4096, 128)
