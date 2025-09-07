
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, query, key, value, inv_scale=None):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale # scaled dot product of the query and key tensors
        attention_weights  = scaled_dot_product.softmax(dim=-1)                    # softmax to compute the attention weights
        output  = attention_weights.matmul(value)                                  # weighted sum of value with attention weights
        return output

# Initializing the model
m  = Model()

# Inputs for the model, these inputs must be different from the initial model (see 'Model') and the input tensor to compute should not be used in the previous model.
query = torch.randn(480)
key   = torch.randn(32, 512, 64) # The dimension of this tensor is important. It must meet the requirements. 
value = torch.randn(32, 512, 64) # These are the values that you want to compute the attention weights and weighted sum with. These tensors must also be different from the initial model (see 'Model').

# Scaling factor for scaling dot product to stabilize gradients
scale = math.sqrt(key.shape[-1])

__output__  = m(query, key, value, inv_scale=scale)

