

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale_factor=0.25, dropout_p=0.1):
        super().__init__()
 
        self.inv_scale_factor  = inv_scale_factor
        self.dropout  = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value): 
        attn_output  = torch.matmul(query / self.inv_scale_factor,
                                     key.transpose(-2, -1))
        attn_output = self.dropout(attn_output)
        return torch.matmul(attn_output, value)


class MultiHeadAttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        num_heads  = 32 
        input_size  =  768  
        head_dimensionality  = 128 

        self.query_projection = torch.nn.Linear(input_size, num_heads *
                                               head_dimensionality)
        
        self.key_projection = torch.nn.Linear(input_size, num_heads
                                              * head_dimensionality)

        self.value_projection = torch.nn.Linear(input_size, 
                                                num_heads * head_dimensionality)
       
        inv_scale_factor=0.25 
        self.scaled_dot = ScaledDotProductAttention(inv_scale_factor
                                                        dropout_p=0.1)

    def forward(self, query):
        v = torch.rand(3, 4, 8)

        vq  = query
        vk  = self.query_projection(vq).view(-1, 4, 
                                               num_heads * head_dimensionality)
        vv  = self.value_projection(v).view(-1, 
                                              vv.size()[-2], 
                                             num_heads * head_dimensionality)

        # Pass the query through a linear transformation before computing 
        # the dot product and softmax. The input_tensor is of size [N, Lq]
        # where N is batch dimension (batch size), and Lq is the sequence length 
        # of the queries
        attn = self.scaled_dot(query=vq, key=vk, value=vv)

        return v


m  = MultiHeadAttentionModel()
 
x1 = torch.rand(32768) 
 
__output__  = m(x1)

__end__

System: 