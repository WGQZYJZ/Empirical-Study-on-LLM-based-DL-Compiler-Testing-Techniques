
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(dim, dim*3, bias=False)
 
    def forward(self, x1, x2):
        v1  = self.qkv(x1).chunk(3, -1) # Compute the output of a linear layer with an embedding dimension of dim
        query, key, value = [_.transpose(-2, -1) for _ in v1]
        scaled_qk  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(16, dim)
x2  = torch.randn(16, dim)
__output__  = m(x1, x2) # The embedding dimension of key and query should be different from the value dimension
