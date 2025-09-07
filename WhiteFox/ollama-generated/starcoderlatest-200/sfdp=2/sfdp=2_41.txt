
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query = self.conv(x1)
        key   = self.conv(x2)
 
        v1 = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_v1 = v1 / scale_factor # Scale the dot product by the inverse scale factor
        softmax_v1 = scaled_v1.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=dropout_p)  # Apply dropout to the softmax output
        output   = dropout_v1 @ value  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 3, 224, 224)
x2 = torch.randn(256, 3, 224, 224)
