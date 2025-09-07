
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)

    def forward(self, x1, x2):
        # Calculate query and key tensors
        k = self.conv2(F.gelu(self.conv1(x1)))

        # Scale dot product by a factor
        qk = torch.matmul(query=x1, key=k, dim=-1)
        scale_factor = F.gelu(self.conv1(x2))

        # Apply softmax to the scaled dot product
        softmax_qk = torch.softmax(scale_factor * qk, dim=-1)  # Softmax on the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output

        # Compute the dot product of the dropout output and the value tensor
        v = dropout_qk.matmul(value=x2)

        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
