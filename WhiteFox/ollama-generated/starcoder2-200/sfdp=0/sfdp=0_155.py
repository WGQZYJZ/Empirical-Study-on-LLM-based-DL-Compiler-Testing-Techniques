
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):
        # Calculate scaled dot product of query and key tensors.
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / inv_scale

        # Compute attention weights as softmax of scaled dot product.
        attention_weights  = scaled_dot_product.softmax(dim=-1)

        # Compute weighted sum using attention weights and value tensor.
        output  = attention_weights.matmul(v)
        return output

# Initializing the model
m = Model()


# Inputs to the model
k1 = torch.randn(4, 50, 768)
v1 = torch.randn(4, 23, 768)
 
__output__  = m(torch.randn(4, 50), k1, v1)
