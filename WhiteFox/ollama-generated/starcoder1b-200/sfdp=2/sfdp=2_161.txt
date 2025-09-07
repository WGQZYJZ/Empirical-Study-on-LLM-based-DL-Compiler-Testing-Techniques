
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        k1 = torch.randn_like(v1) # Generate a random tensor with normal distribution with the same shape as the input tensor
        k2 = torch.randn_like(v1)
        v2 = (k1 + k2)/2  # Compute the sum of the two random tensors
        s1 = torch.softmax((v1 - v2), dim=-1)  # Apply softmax to the difference between the input and the computed dot product
        dropout_s1 = torch.nn.functional.dropout(s1, p=dropout_p)  # Apply dropout to the softmax output
        v3 = dropout_s1.matmul(x1)  # Compute the dot product of the dropout output and the value
        return v3


# Initializing the model
m = Model()


# Inputs to the model
v1 = torch.randn(1, 8, 64, 64)  # Generate a random tensor with normal distribution with the same shape as the input tensor
