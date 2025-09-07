
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        inv_scale_factor = 1 / (self.conv1(x1).pow(2) + self.conv2(x1).pow(2))
        softmax_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v1 = self.conv1(dropout_qk)  # Apply convolution on the output of the dropout
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()

