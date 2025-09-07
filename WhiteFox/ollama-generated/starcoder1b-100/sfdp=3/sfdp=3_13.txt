
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, v1.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scale_factor = torch.sqrt(torch.nn.functional.softplus(qk))  # Scale the dot product by a factor
        softmax_qk = qk.mul(scale_factor).softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(v2)


# Initializing the model
m = Model()


