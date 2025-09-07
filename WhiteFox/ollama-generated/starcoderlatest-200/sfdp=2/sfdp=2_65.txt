
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, mask=None, inv_scale_factor=0.125, dropout_p=0.1):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        if mask is not None:
            masked_output = mask * output + (1 - mask) * (-1e30)
            return masked_output
        else:
            return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(5, 64, 7, 7)
key = torch.randn(5, 8, 7, 7)
value = torch.randn(5, 8, 7, 7)
mask = None # Set mask as none in the code block above to avoid unnecessary computation.
inv_scale_factor=0.125 # Use a scale factor of 0.125 in this example
dropout_p = 0.1 # Use dropout probability of 0.1 in this example


# Expected output: tensor(-1e+30, -1e+30, -1e+30, -1e+30,  8.469)
