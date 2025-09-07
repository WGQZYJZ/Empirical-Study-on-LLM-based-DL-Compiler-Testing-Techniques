
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):

        # Compute scaled dot product attention
        scale  = (k.shape[-1] ** -0.5)
        attentions = torch.matmul(q, k.transpose(-2, -1)) * scale
 
        # Apply the softmax to the scaled dot product
        weights = attentions.softmax(dim=-1)
 
        # Compute the output of attention mechanism as weighted sum of values
        output  = weights.matmul(v)
        return output


# Initializing the model
m  = Model()
 
# Inputs to the model
input_query  = torch.randn(4, 8)
input_key  = torch.randn(4, 512, 640) # In real scenario query and key tensors will be of different sizes due to batching
input_value  = torch.randn(4, 512)
 
__output__  = m(input_query, input_key, input_value)
