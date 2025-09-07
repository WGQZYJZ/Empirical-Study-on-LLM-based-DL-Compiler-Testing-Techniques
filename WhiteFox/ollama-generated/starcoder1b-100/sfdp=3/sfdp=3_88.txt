
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(3, 8, 64))
        self.key   = torch.nn.Parameter(torch.randn(2, 8, 64))
        self.scale_factor = 0.5
 
    def forward(self, x1):
        query_v = self.query  # Use a parameter to share the same value of query tensor for different layers in the model
        key_v   = self.key
     
        kq = torch.matmul(query_v, key_v)  # Compute the dot product of the query and key tensors
        scaled_qk = kq.mul(self.scale_factor)  # Scale the dot product by a factor

        softmax_qk = scaled_qk.softmax(-1)  # Apply softmax to the scaled dot product

        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        y  = dropout_qk.matmul(x1)
     
        return y


# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(3, 8, 64)
key   = torch.randn(2, 8, 64)
