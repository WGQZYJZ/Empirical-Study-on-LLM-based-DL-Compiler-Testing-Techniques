import torch
import torch.nn as nn
import torch.nn.functional as F

class Attention(torch.nn.Module):
    def __init__(self, num_heads=8, key_dim = 64, value_dim=128, dropout_rate =0.5):
        super().__init__()
        
        self.num_heads = num_heads
        self.dropout_rate = dropout_rate
        
        self.key_dim = key_dim 
        self.value_dim = value_dim 
        
        # We assume the embedding dimension is divisible by number of heads and that 
        # the sequence length is equal to batch size for simplicity 
        self.scale_factor = float(self.key_dim ** -0.5)
        self.att_weighting = nn.Linear(value_dim, num_heads*num_heads)
        
    def forward(self, query, key, value):

        # Input dimension is [seq length x batch size x embedding dim] 
        seq_length  = query[0].shape[-1]
        batch_size  = query[0].shape[0]
        
        # We assume the embedding dimension is divisible by number of heads and that 
        # the sequence length is equal to batch size for simplicity 
        key_dim = int(self.key_dim/ self.num_heads)
        value_dim=int(self.value_dim / self.num_heads)
        
        # Calculate scaled dot product
        query_reshape  = torch.reshape(query, (seq_length*batch_size, -1))
        key_reshape    = torch.reshape(key,(seq_length*batch_size,-1)).transpose(-2,-1).clone()
        value_reshape  = torch.reshape(value,(seq_length*batch_size,-1)).clone()
        
        # Use scaled dot product to calculate attention weights 
        scaled_dot_product= torch.matmul(query_reshape, key_reshape) / self.scale_factor
        attentions        = F.softmax(scaled_dot_product, dim=-1)

        # Calculate output as weighted sum of values 
        out =torch.bmm(attentions , value_reshape).reshape((batch_size,-1))
        
        return out
    
class Model(nn.Module):
    def __init__(self):
        super().__init__()
       
        # Initializing the model 
        m= torch.randn(64, 320)
        k =torch.randn(m.shape[0], m.shape[-1])

        self.attentions = Attention()
        self.
