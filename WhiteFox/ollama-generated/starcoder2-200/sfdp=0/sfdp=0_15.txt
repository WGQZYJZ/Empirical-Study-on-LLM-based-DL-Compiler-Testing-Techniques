
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / np.sqrt(50)
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(v)
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
q  = torch.randn([3,50])
k  = torch.randn([3,50])
v  = torch.randn([3,24])
 
__output__  = m(q, k, v)

