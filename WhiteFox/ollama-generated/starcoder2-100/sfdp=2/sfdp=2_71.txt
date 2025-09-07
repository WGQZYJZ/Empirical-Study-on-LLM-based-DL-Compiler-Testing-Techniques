
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(32, 8)

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, dropout_p=0.1, inv_scale_factor=None):
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk / 32 if inv_scale_factor is None else qk.div(inv_scale_factor) # Scale the dot product by an inverse scale factor

        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
 
        output  = dropout_qk.matmul(value)# Compute the dot product of the dropout output and a value
        return output

# Initializing the model with initial inputs and parameters
m = Model()
q = torch.randn(32, 10) # Input query
k = torch.randn(32, 8, 32) # Input key
v = torch.randn(32, 4, 576) # Input value

