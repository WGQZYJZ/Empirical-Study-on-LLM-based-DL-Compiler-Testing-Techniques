
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key  = torch.nn.Parameter(torch.rand((2, 3), requires_grad=True))
        self.value  = torch.nn.Parameter(torch.rand((4, 3)), requires_grad=True)
    
    def forward(self, query):
        inv_scale_factor  = self.key.shape[0] * (1 / math.sqrt(int(self.key.shape[-1])) ) ** -2
        qk  = torch.matmul(query, self.key.transpose(-2, -1))
        scaled_qk  = qk.div(inv_scale_factor)
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.75) 
        output  = dropout_qk.matmul(self.value)
        return output

# Initializing the model
m  = Model()

# Inputs to the model
query1  = torch.randn((4), requires_grad=True) # query is a batch of inputs with dimension (4, )
__output__  = m(query1)