

import torch

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=1., bias=0.) -> None:
        super().__init__()
        self.inv_scale = torch.nn.Parameter(
            torch.tensor(
                inv_scale, dtype=torch.float), requires_grad=False)

        self.bias  = torch.nn.Parameter(
            torch.tensor(
                bias, dtype=torch.float), requires_grad=False
        )
 
    def forward(self, q, k, v):

        # Compute scaled dot product of query and key tensors.
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / self.inv_scale
        
        # Add bias to the scaled dot product.
        scaled_dot_product += self.bias 
 
        # Compute attention weights using softmax on the last dimension of the scaled 
        # dot product tensor.
        attention  = scaled_dot_product.softmax(dim=-1)

        # Compute output by multiplying value with the attention weights.
        output  = attention.matmul(v)
        
        return output

class Model(torch.nn.Module):
    def __init__(self, inv_scale=0.75):
        super().__init__()
        self._scaled_dot_product_attention = ScaledDotProductAttention(inv_scale)
 
    def forward(self, query, key, value):
        return self._scaled_dot_product_attention(query, key, value)


# Initializing the model
model  = Model()
# Inputs to the model. Make sure the inputs are the same as in previous test case.
q1  = torch.randn(4, 4396)
k1  = torch.randn(4, 2507)
v1  = torch.randn(4, 8192)

