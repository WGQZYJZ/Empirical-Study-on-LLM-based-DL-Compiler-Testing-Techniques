
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, query):
        k = self.linear(query).transpose(-2, -1) 
        v = self.linear(query).transpose(-2, -1) 
        qk = torch.matmul(query, k)
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output = dropout_qk.matmul(v)
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
 query = torch.randn(128, 10)
__output__  = m(query)
