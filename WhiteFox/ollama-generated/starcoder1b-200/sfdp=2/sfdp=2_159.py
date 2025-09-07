
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(d_k, d_k)
        self.key   = torch.nn.Linear(d_k, d_k)
        self.value = torch.nn.Linear(d_v, d_v)

    def forward(self, x1):
        query  = self.query(x1).permute(0, 2, 1)  # Permutation of the input tensor is used to form the keys and values
        key    = self.key(x1).permute(0, 2, 1)
        value  = self.value(x1).permute(0, 2, 1)
        dot    = torch.matmul(query, key)  # Compute the dot product of the query and the keys
        scaled_dot = dot.div(self.scale_factor)  # Scale the dot product by the inverse scale factor
        softmax  = scaled_dot.softmax(-1)  # Apply softmax to the scaled dot product
        dropout = torch.nn.functional.dropout(softmax, p=dropout_p)  # Apply dropout to the softmax output
        return torch.matmul(dropout, value)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 512)
