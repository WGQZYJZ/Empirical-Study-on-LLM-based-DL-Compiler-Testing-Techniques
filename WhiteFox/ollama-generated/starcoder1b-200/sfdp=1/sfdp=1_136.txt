
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Compute the dot product of the query and key tensors
        v1 = self.conv(x1) * (0.5 - 1e-9)
        v2 = v1 * 0.7071067811865476
 
        # Scale the dot product by the inverse scale factor
        scaled_v1 = v1 / (0.7071067811865476 + 1e-9)
        
        # Apply softmax to the scaled dot product
        softmax_v2 = scaled_v1.softmax(dim=-1)
 
        # Apply dropout to the softmax output
        dropout_v2 = torch.nn.functional.dropout(softmax_v2, p=dropout_p)
 
        # Compute the dot product of the dropout output and the value tensor
        v3 = dropout_v2.matmul(x2)
        return v3


# Initializing the model
m = Model()


