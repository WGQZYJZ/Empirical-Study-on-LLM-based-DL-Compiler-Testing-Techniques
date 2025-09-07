
class Model(torch.nn.Module):
    def __init__(self, inv_scale=0.5126378491523823):
        super().__init__()
 
        self.inv_scale = torch.tensor(
            inv_scale)
 
    def forward(self, query, key, value):
        scaled_dot_product  = (torch.matmul(query,
                                            key.transpose(-2, -1)) /
                              self.inv_scale).softmax(dim=-1)
 
        attention_weights = scaled_dot_product

        output  = attention_weights.matmul(value)
        return output


# Initializing the model with a custom value of the scaling factor `inv_scale` (the same scale used in OpenAI GPT-2)
m = Model(0.5126378491523823)
 
# Inputs to the model 
q = torch.randn(2, 32, 64)
k = torch.randn(2, 64, 32)
v = torch.randn(2, 64, 64)

 # Output of the model on custom inputs
out1  = m(q, k, v)

# Inputs to the model with a different value for the scaling factor `inv_scale` (a small scale used in the model used by OpenAI GPT-2)
m = Model(0.5126378491523823 / 10.0)
 

 # Output of the model on custom inputs with a different value for scaling factor `inv_scale` (a small scale used in the model used by OpenAI GPT-2)
out2  = m(q, k, v)
