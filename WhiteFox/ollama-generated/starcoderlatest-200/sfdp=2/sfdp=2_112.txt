
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(512, 256)
        self.k = torch.nn.Linear(512, 256)
        self.v = torch.nn.Linear(512, 256)
 
    def forward(self, q1, k1):
        v1 = self.v(torch.cat([q1, k1], dim=-1))
        k1 = self.k(q1)
        q1 = self.q(v1)
        __output__  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        __output__  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return __output__


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(2, 512, 64, 64)
k1 = torch.randn(2, 512, 64, 64)
