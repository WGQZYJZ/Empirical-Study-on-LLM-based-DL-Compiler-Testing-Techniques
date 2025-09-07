
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        qk = torch.matmul(v2, torch.transpose(v1, -2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(0.7071067811865476)  # Scale the dot product by a factor
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)  # Apply dropout to the softmax output
        v6 = dropout_qk.matmul(v5)  # Compute the dot product of the dropout output and the value tensor
        return v6


# Initializing the model
m = Model()


