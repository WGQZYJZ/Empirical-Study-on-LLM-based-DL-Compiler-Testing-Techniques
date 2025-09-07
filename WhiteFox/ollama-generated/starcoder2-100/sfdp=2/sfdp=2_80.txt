
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m  = Model()
 
# Input to the model (shape: [batchsize, inputdimension])
query  = torch.randn([1024, 768], requires_grad=True)
key   = torch.randn([1024, 768], requires_grad=True)
value = torch.randn([1024, 998])
 
# Compute model outputs with provided inputs
__outputs__ = m(query, key, value)

