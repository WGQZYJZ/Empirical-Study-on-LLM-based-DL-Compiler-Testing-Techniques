
import torch 
import torch.nn as nn 

class MyModel(nn.Module):
    def __init__(self, attn=None) -> None:
        super().__init__()
        self.attn = attn

    def forward(self, query, key, value, attn_mask):

        qk  = (query @ key.transpose(-2,-1)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors 
        qk += attn_mask # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value tensor

        return self.attn(output), output

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.mymodel  = MyModel()
 
    def forward(self, attn_mask=None):
        q1   = torch.randn([24,385]) # Initialize the query tensor with shape [batch_size, embedding_size] 
        k1   = torch.randn([24,769*769]) # Initialize the key tensor with shape [batch_size, channel * channel]
        v1  = torch.randn([24,385,769*769])  # Initialize the value tensor with shape [batch_size, output_channels, num_filters] 
        __output__, 