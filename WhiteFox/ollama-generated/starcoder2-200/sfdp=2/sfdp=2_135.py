
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor, dropout_p=0.1):
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk  = qk / inv_scale_factor
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(value)

# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(256, 1024)
key    = torch.randn(256, 1024)
value  = torch.randn(256, 128)
 
# Parameters for scaling factor and dropout probability in the model
scale_factor  = m._modules["-2"][-3]["-3"].weight.detach().norm() * 1e+4
dropout_prob = m._modules["-2"][0].p
__output__  = m(query, key, value, scale_factor)

