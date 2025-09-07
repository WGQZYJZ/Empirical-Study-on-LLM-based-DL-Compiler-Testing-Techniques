
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_, dropout_p=0.1, inv_scale_factor_=2):
        # Compute the dot product of the query and the key
        qk  = torch.matmul(query_, key_.transpose(-2,-1))
 
        scaled_qk  = qk / inv_scale_factor_
    
        softmax_qk = scaled_qk.softmax(dim=-1)

        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 

        output = dropout_qk.matmul(value_)
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
query_ = torch.randn(4321, 7856, requires_grad_=True)
key_   = torch.randn(9876, 4096, requires_grad_=True)
value_ = torch.randn(7654, 9012, requires_grad_=True)

 # Output of the model
output  = m(query_, key_, value_)