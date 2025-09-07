
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk, value, key=None, query=None, inv_scale_factor=None, dropout_p=None):
        if query is None and key is not None:
            query  = key
 
        v1 = torch.matmul(query, key.transpose(-2, -1)) 
        v2 = v1 / inv_scale_factor
        v3 = v2.softmax(dim=-1) 
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)  
        return v4.matmul(value)


# Initializing the model
m  = Model()
 
# Inputs to the model
qk = torch.randn(256, 2048, 17).to(torch.float32)  # query, key tensors with shape (batch_size, size of the embedding layer, number of heads)
value = torch.randn(256, 896, 19 * 1024)  # value tensor with shape (batch_size, size of the hidden layer, the total length of tokens in all batches)
 
if dropout_p is not None:
    qk *= inv_scale_factor
    softmax = torch.nn.functional.dropout(qk.softmax(-1), p=dropout_p) 
    v4 = value * softmax  # shape (batch_size, size of the hidden layer, total length in all batches * number of heads)
else: 
    v3 = qk / inv_scale_factor  
    v5 = v3.softmax(dim=-1)  # shape (batch_size, size of the embedding layer, number of heads)
    v4 = value * v5

