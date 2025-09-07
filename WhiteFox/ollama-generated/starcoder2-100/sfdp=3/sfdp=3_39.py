
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Add the dropout operation 
        output  = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()
 
# Query tensor for the model
query = torch.randn(2048, 100) 
 
# Key tensor for the model
key  = torch.randn(32768, 100) 
 
# Value tensor for the model
value  = torch.randn(32768, 768) 

__output__  = m(query, key, value)

