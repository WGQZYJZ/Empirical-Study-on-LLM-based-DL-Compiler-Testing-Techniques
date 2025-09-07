
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 16)
        self.key = torch.nn.Linear(4096, 512)
        self.value = torch.nn.Linear(4096, 512)

    def forward(self, x):
        query_x = self.query(x).transpose(-2, -1) # Transpose the query vector for softmax operation
        key_x  = self.key(torch.rand(32*32, 4096)) # Generate the key vector
        value_x  = self.value(torch.rand(512*32*32, 4096))

        qk  = torch.matmul(query_x, key_x)  # Compute the dot product of the query and the key
        scaled_qk = qk.div(scale_factor=2**-7.) # Scale the dot product by an inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product

        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5, training=self.training) # Apply dropout to the softmax output

        output  = dropout_qk.matmul(value_x) # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = AttentionModel()

