
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x, k, v):
        qk = torch.matmul(x, k.transpose(-2, -1))  # Compute the dot product of the query and the key
        inv_scale_factor = (
            torch.rsqrt((torch.pow(qk, 2) + torch.pow(k, 2))) * self.dropout_p
        )  # Scale the dot product by the inverse scale factor
        softmax_qk = qk / (self.dropout_p * inv_scale_factor)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output

        output = dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value

        return output


# Initializing the model
m = Model()

