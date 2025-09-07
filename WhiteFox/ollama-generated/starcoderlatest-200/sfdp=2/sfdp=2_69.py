
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Input to the model
query  = torch.randn(4, 32, 64, 64)
key    = torch.randn(4, 32, 64, 64)
value  = torch.randn(4, 32, 64, 64)
inv_scale_factor  = torch.ones(4, 1, 1, 1) * 1e-8 # Compute the inverse of the scale factor
dropout_p         = 0.5                          # Set the dropout probability to 0.5
__output__        = model(query, key, value, inv_scale_factor, dropout_p)

