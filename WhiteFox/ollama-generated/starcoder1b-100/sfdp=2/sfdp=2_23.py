
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_layer  = torch.nn.Linear(768, 1024)
        self.key_layer    = torch.nn.Linear(768, 1024)
        self.value_layer  = torch.nn.Linear(1024, 512)
        self.scale         = torch.nn.Parameter(torch.randn(1024))
        self.softmax      = nn.Softmax()

    def forward(self, x):
        # Compute the dot product of the query and the key
        query = self.query_layer(x)
        key   = self.key_layer(x)

        # Scale the dot product by the inverse scale factor
        scaled_qk = torch.div(torch.mul(query, key), torch.mul(self.scale, 1024))
        
        # Apply softmax to the scaled dot product
        qk = self.softmax(scaled_qk)

        # Apply dropout to the softmax output
        d = torch.nn.functional.dropout(qk, p=dropout_p)

        # Compute the dot product of the dropout output and the value
        return d.matmul(self.value_layer(x))


# Initializing the model
m = Model()


