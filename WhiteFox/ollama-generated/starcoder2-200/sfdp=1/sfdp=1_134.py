
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Parameter(torch.randn(3, 10)) 
        self.key   = torch.nn.Parameter(torch.randn(27568, 194))
        self.value = torch.nn.Parameter(torch.randn(27568, 194))

    def forward(self):
        qk  = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk  = qk / inv_scale_factor
        softmax_qk  = scaled_qk.softmax(dim=-1) 
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output      = dropout_qk.matmul(value)

        return output

# Initializing the model
m  = Model()
__output__    = m()

