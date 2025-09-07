
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(torch.Tensor([0]))
 
        self.att = torch.nn.MultiheadAttention(128, 4)
 
    def forward(self, query: Tensor, key: Tensor, value: Tensor):
        scaled_qk = (query * key).mul_(
            0 if self.scale is None else self.scale
        )
        dropout_qk = torch.nn.functional.dropout(scaled_qk.softmax(-1), p=0.2)
 
        return dropout_qk.matmul(value)


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(3, 4, 64)
key    = torch.randn(3, 4, 64)
value  = torch.randn(3, 8, 128)
 
__output__  = m(query, key, value)