
class Model(torch.nn.Module):
    def __init__(self, inv_scale=10):
        super().__init__()
        self.inv_scale = inv_scale
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
q = torch.randn(32, 64, 50, 1024).normal_()
k = torch.randn(32, 64, 1024, 768)
v = torch.randn(32, 64, 50, 768)

 # Initializing the model parameters with random values and then assigning them to the module’s `weight` attribute:
w_query, w_key, w_value  = [torch.rand((1,), requires_grad=True)] * 3
w  = torch.nn.ParameterList([w_query, w_key, w_value])
 
 # Updating the model parameters based on a backpropagation pass:
(m.inv_scale.data  += torch.randn(*w[0].shape) / 1e4).clamp_(1/512., 3.)

