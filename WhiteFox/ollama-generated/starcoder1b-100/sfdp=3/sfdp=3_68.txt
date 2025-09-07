
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(512, 2048, 1)
        self.key_conv = torch.nn.Conv2d(512, 2048, 1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(0.5)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v1 = self.query_conv(x1).transpose(-2, -1) * 0.5  # Multiply the query tensor by the factor `0.5` and transpose the dimensions
        v2 = v1 * 0.7071067811865476  # Multiply the `v1` by `0.7071067811865476`
        output = dropout_qk.matmul(v2)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


