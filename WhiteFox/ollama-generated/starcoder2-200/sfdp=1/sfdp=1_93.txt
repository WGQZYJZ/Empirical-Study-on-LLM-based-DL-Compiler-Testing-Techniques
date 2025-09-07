
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Parameter(torch.randn(4, 3), requires_grad=True)
        self.key   = torch.nn.Parameter(torch.randn(512*7 * 7, 60))
        self.value  = torch.nn.Parameter(torch.randn(512, 98*7 * 7), requires_grad=True)
 
    def forward(self):
        qk = torch.matmul(self.query, self.key.transpose(-2, -1))
        scaled_qk  = qk.div(inv_scale_factor) # Scale the dot product by an inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output = dropout_qk.matmul(self.value)

# Initializing the model with random values
m = Model()

 # Inputs to the model
__output__  = m()

