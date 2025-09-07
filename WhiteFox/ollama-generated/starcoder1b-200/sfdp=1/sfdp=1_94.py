
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.query = torch.nn.Parameter(torch.randn(64))
        self.key   = torch.nn.Parameter(torch.randn(64, 64))
        self.scale_factor = torch.exp(0)
        
    def forward(self, x):
        qk = torch.matmul(x, self.query.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        inv_scale_factor = 1 / math.sqrt(self.key.size(-1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        y = dropout_qk.matmul(x)
        return y

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
