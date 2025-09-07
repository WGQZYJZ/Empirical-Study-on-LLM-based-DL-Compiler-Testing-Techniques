
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(8) # Scaled dot product attention
        attention_weights  = scaled_dot_product.softmax(dim=-1) 
        output             = attention_weights.matmul(v)
        return output

# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(3, 8, 4096).to('cuda')
k = torch.randn(2, 7, 8, 4096) # Keys for the Scaled Dot-Product Attention Mechanism
v = torch.randn(10, 5, 4096) # Values for the Scaled Dot-Product Attention Mechanism

__output__  = m(q, k, v).to('cuda')

