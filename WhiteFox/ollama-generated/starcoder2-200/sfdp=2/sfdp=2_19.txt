
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Parameter(torch.randn(128, 3))
 
    def forward(self, query):
        value  = 2 * self.key
        v1 = torch.matmul(query, self.key.transpose(-2, -1)) 
        scaled_v1  = v1 / inv_scale_factor
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v4 = dropout_qk.matmul(value)
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
query  = torch.randn(1280, 3).requires_grad_()


__output__  = m(query)
 

