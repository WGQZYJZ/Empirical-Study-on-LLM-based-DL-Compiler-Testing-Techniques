

import torch
 
# model: scaled dot-product attention.
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    # Initialize the module with two linear transformations and one bias term. The weights of these transformation maps will be initialized randomly from a uniform distribution in the interval [−0.5, 0.5], while the bias term will be set to 1. The activation functions used for the first linear transformations are ReLU, and those used for the second linear transformation are GELU or SiLU (smoothly scaled sigmoid) by default.
    def init_weights(self):
        torch.nn.init.uniform_(self.attn, -0.5, 0.5)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        # Compute the dot product of the query and transposed key matrices and divide by the square root of their dimension (the scaling factor).
        scaled_dot = self.attn(query @ key.transpose(-2,-1)) / key.size()[-1].sqrt()
        # Apply softmax to the result using the last axis as the target, resulting in a tensor of same shape with elements normalized by their sum across that axis.
        attn_weights = scaled_dot.softmax(dim=-1)
 
        # Compute the output by multiplying the weights with values.
        out = attn_weights @ value
        return out


# Initializing the model
m  = ScaledDotProductAttention()
 
# Inputs to the model
query = torch.randn(3, 4096)
key   = torch.randn(3, 1280)
value = torch.randn(3, 512, 1280)
 
m.init_weights()
output = m(query, key, value).shape
