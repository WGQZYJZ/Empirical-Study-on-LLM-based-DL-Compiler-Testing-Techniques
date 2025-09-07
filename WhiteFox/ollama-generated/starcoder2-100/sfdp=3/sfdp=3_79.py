
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled = torch.matmul(query, key.transpose(-2, -1)) * scale
        output  = torch.nn.functional.dropout(softmax(scaled), p=p) @ v


# Initializing the model
m  = Model()
 
# Inputs to the model
scale_factor = 0.7834569820981762
scale = torch.rand(query.size(-2)) * scale_factor + scale_factor
softmax = torch.nn.Softmax(-1)
p = 0.8595870173338417
q, k, v= torch.randn(scale, query.size(-1)),  torch.randn(key.size()),   value = torch.randn(value.size() -2, query.size(-1))

 # The model will be different from the previous one and will generate a new random input tensor.
__output__  = m(q[None], k[:, None, :], v)
