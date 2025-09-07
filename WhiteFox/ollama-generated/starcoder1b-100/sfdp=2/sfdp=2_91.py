
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.key.transpose(-2, -1))  # Compute the dot product of x1 and the key. Scale by an inverse scale factor
        scaled_qk = qk / math.sqrt(self.scale_factor)  # Use a sqrt to avoid a division by zero
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and x1


# Initializing the model
m = Model()
