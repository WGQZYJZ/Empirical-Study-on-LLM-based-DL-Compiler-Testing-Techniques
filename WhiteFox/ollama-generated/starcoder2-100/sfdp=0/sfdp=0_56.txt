

import torch
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self):
        scaled_dot_product  = self.query @ self.key.T / (torch.sqrt(self.scale))
        attention_weights   = scaled_dot_product.softmax(-1)
        return attention_weights, self.value @ attention_weights.T


# Initializing the model
m  = Model()
 
# Inputs to the model

m.query         = torch.randn(2048, 65793, requires_grad=True).cuda() * (1 / m.scale) ** .5;     # [batch_size x n_head x num_queries]
m.key           = torch.randn(m.n_head, <KEY> * m.scale);     # [n_head x num_keys x dim_q_k]
m.value         = torch.randn(2048, 65793)
 
__output__, out1  = m()

out2  = m().softmax(-1).T @ m.value

