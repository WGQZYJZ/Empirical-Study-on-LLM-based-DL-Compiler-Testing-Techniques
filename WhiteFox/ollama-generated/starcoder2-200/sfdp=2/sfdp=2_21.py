
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.randn(256, 490) # Initialize the query matrix
        self.key  = torch.randn(387, 128) # Initialize the key matrix
 
    def forward(self, x1):
        v1  = torch.nn.functional.normalize(self.query) 
        v2  = torch.nn.functional.normalize(self.key) 
        v4  = torch.matmul(v1, v2.transpose(-2, -1)) / 7.0569837e-05
        v5  = scaled_qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        v7  = v4.softmax(dim=-1) 
        v8  = torch.nn.functional.dropout(v7, p=dropout_p) # Apply dropout to the softmax output
        v9  = self.value * v5  # Compute the dot product of the dropout output and the value
        return v6


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(2, 4) 


__output__  = m(x1)
