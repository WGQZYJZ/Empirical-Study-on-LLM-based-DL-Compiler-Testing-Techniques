
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax  = torch.nn.Softmax(-1)
 
    def forward(self, query, key, value):
        scaled_qk  = torch.matmul(query, key.transpose(-2, -1)) * scale_factor
        softmax_qk  = self.softmax(scaled_qk)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output  = dropout_qk.matmul(value)
        return output


# Initializing the model
m  = Model()
 
 
 # Inputs to the model
query   = torch.randn(16384, 5720) * scale_factor
key    = query
value  = query
 
 
__output__  = m(query, key, value)
