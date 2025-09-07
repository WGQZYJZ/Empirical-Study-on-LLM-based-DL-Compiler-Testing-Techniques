
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and the key
        scale_factor = torch.rsqrt(torch.abs(qk))  # Scale by the square root of the dot product
        softmax_qk = qk / (scale_factor * math.sqrt(dim=x1.shape[2]))  # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        y  = dropout_qk.matmul(y)  # Compute the dot product of the dropout output and a value
        return y


# Initializing the model
m = Model()


