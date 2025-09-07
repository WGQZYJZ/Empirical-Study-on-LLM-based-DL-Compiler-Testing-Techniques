
class SelfAttention(torch.nn.Module):
    def __init__(self, dim=32):
        super().__init__()
        self.qkv = torch.nn.Linear(dim, 3 * dim)
 
    def forward(self, input):
        qkvw  = self.qkv(input).transpose(-1, -2) # Flatten the input tensor and then transpose to reshape it to be of shape [batch_size, length_of_sequence, 3 * dim]
        query  = qkvw[..., :dim] 
        key   = qkvw[..., dim: dim*2]
        value = qkvw[..., -dim:]
        qkv  = (query.matmul(key.transpose(-1, -2)) / math.sqrt(query.size(-1))).softmax(-1) # Compute the dot product of query and key tensors and scale them by 1/sqrt(dimension_of_sequence). Then apply softmax to these scaled dot products.
        dropout_qkv = torch.nn.functional.dropout(qkv, p=0.75) 
        output  = dropout_qkv.matmul(value) # Compute the dot product of dropout outputs and value tensor. 
        return output
