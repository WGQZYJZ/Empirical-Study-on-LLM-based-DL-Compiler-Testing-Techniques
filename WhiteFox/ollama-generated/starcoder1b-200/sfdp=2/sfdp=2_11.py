
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        qk  = torch.matmul(v1, v1.transpose(-2, -1))  # Compute the dot product of two matrices
        scaled_qk = qk.div(torch.sqrt(torch.clamp(torch.max(qk), min=1e-8)))  # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v2 = dropout_qk.matmul(value)  # Compute the dot product of two matrices
        return v2


# Initializing the model
m = Model()


