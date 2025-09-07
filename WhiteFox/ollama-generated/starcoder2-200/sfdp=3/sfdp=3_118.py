
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0.1):  # Dropout probability p is a hyperparameter
        scale_factor = torch.ones(()) + 5e-6  # Scale factor
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output  = dropout_qk.matmul(value) 
        return output
 
# Initializing the model
m = Model()

 # Inputs to the model
query  = torch.randn((1024, 384))
key  = query + 5e-6
value  = key * -9  # Value tensor
 
__output__  = m(query=query, key=key, value=value)

