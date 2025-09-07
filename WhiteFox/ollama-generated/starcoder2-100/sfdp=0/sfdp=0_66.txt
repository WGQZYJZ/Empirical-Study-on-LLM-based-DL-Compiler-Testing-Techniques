
import torch
import torch.nn as nn
 
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model=512, num_heads=8, dim_k=64):
        super().__init__()
 
        self.num_heads = num_heads
        self.d_head  = int(d_model / num_heads)
        self.dropout = nn.Dropout()
        self.linear_query = nn.Linear(dim_k * d_model, d_model)
        self.linear_key = nn.Linear(dim_k * d_model, d_model)
        self.linear_value = nn.Linear(d_head * 32, d_model)
        self.output_linear = nn.Linear(num_heads*self.d_head, num_heads*d_model)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
 
        batch_size  = query.shape[0]
        q = self.linear_query(query).reshape(batch_size, -1 , d_head, num_heads)
        k = self.linear_key(key).reshape(batch_size, -1 , d_head, num_heads)
        v = self.linear_value(value)
 
        q = torch.transpose(q, 0, 1) # batch size * seq length * dim/head * num heads
        k = torch.transpose(k, 0, 1) # batch size * seq length * dim/head * num heads
        v = torch.transpose(v, 0, 1) 
 
        scaled_dot_product = torch.matmul(q , torch.transpose(k ,-2,-3)) / (d_head ** -0.5) 
        attention_weights = scaled_dot_product.softmax(-1).detach()
        output = self.output_linear(attention_weights @ v )
 
        
        return output
# Initializing the model
m  = MultiHeadAttention().to('cpu')


# Inputs to the model
query = torch.randn((256,300))
key   = query.clone()
value = key + torch.ones(1)
