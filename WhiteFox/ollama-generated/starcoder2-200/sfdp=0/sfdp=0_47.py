
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1): 
        scaled_dot_product  = torch.matmul(q1, k1.transpose(-2,-1)) / math.sqrt(d_k)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v1)

# Initializing the model
m  = Model()

 # Inputs to the model
 q1, k1, v1  = torch.randn(32, d_k), torch.randn(32, d_k), torch.randn(32, dq_out)
 
 # Call the model: generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements
 __output__  = m(q1, k1, v1).to_list()

