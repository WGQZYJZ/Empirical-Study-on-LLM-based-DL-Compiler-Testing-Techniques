In this example, the `ScaledDotProductAttention` module implements the Scaled Dot-Product Attention mechanism. We can see that in `forward`, the scaled dot product between query and key tensors is computed, which is multiplied by the temperature constant 1/temperature (if temperature is not None), followed by applying a softmax over the dimensions specified by dim. The attention weights are then used to compute a weighted sum of the value tensor as output.


# Description of requirements
The model should contain the following pattern:
This pattern characterizes the Self-Attention mechanism. In this mechanism, a softmax layer is applied to the product of query, key and value tensors with scale 0.95 for each dimension, then used to compute the attention weights between query and key tensors. This results in a weighted sum of the value tensor as output.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = SelfAttention()
 
    def forward(self, query, value, key):
        attention_weights  = torch.matmul(q, k.transpose(-2, -1)) / scale
        output = attention_weights.matmul(v)
        return output

class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):
        attention_weights  = torch.matmul(q, k.transpose(-2, -1)) / scale
        output = attention_weights.matmul(v)
        return output
output = self_attn((x,))  # x.shape = (32, 8, 64, 64)
attention_weight = 0.5 * (torch.matmul(query, key[i]) + torch.matmul(key[i], query) \
                        - torch.matmul(query, key[i].transpose(-2, -1)))


# Description of requirements
The model should contain the following pattern:


