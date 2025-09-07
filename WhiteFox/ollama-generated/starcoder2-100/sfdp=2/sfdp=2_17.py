
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_=None, inv_scale_factor=1., dropout_p=0., p2d=False):
        qk = torch.matmul(query_, key_.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)   # Apply softmax to the scaled dot product
        if dropout_p != 0.:
            dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        else:
            dropout_qk = softmax_qk
        output = dropout_qk.matmul(value_)   # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(4, 80)
key    = torch.randn(160, 50)
value_ = torch.randn(160, 239)
inv_scale_factor = .7
dropout_p        =  0

__output__  = m(query_, key_, value_=None, inv_scale_factor=1., dropout_p=0., p2d=False)

