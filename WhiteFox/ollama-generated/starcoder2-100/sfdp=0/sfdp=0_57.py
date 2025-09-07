

import torch 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__() 
        self._scale = float(8)
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) / self._scale ** 0.5 #TODO: define this parameter as a constant
        attention_weights   = scaled_dot_product.softmax(dim=-1) 
        output              = attention_weights.matmul(value)
        return output

