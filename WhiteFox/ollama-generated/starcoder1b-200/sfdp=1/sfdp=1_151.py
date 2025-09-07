
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Query is not an input tensor because the dimensionality of query and key should be different.
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(128)  # Compute the dot product of x1 and x2. Then compute the inverse scale factor by dividing by sqrt(128).
        scaled_qk = qk / math.sqrt(128)  # Apply softmax to the scaled dot product.
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)  # Apply dropout to the softmax output.
        return dropout_qk.matmul(x3)  # Compute the dot product of the dropout output and x3.


# Initializing the model
m = Model()


