
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
        qk  = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output  = dropout_qk.matmul(value)
        return output

 # Initializing the model
m  = Model() 

 # Inputs to the model 
 query  = torch.randn(16384, 572096)
 key   = torch.randn(16384, 572096)
 
 # Scaled query and key tensors with shape [batch_size, query_length, 1] and [batch_size, 1, key_length]. 
 scale_factor = torch.tensor([0.1])
 dropout_p   = 0.3

 value = torch.randn(2048, 572096)
 
 # Initializing the parameters for scaled query and key tensors with shape [batch_size, 1] and [batch_size, 1]. 
 scale_factor[None], dropout_p[None]
 
 # Compute the output. The result will have a shape of [batch_size, query_length, key_length]
 output = m(query, key)
 