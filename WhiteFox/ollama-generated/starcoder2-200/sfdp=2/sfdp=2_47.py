
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query):
        k = torch.randn((16, 8))
        v = torch.randn((16, 32, 512))
        scale_factor = 4096 # Set the scaling factor to 4096 here in practice
        dropout_p = 0.7 # Set the dropout probability to 0.7 here in practice
 
        qk = torch.nn.functional.linear(query, k)
        scaled_qk = qk / scale_factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
 
        v1  = v[None] * dropout_qk[:, None] # Apply broadcasting to the value
        v2  = v1.sum(-3).div_(dropout_qk.shape[-1]) # Compute the weighted average of the dropout output and the value
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
