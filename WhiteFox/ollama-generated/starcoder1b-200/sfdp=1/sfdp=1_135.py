
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, k1):
        # Compute the dot product of the query and key tensors
        v1 = self.conv(x1)
        v2 = (k1 * v1).softmax(dim=-1)  # Apply softmax to the scaled dot product

        # Dropout to prevent the network from becoming unstable
        dropout_qk = torch.nn.functional.dropout(v2, p=self.dropout_p)
        
        # Compute the dot product of the dropout output and the value tensor
        v3 = dropout_qk.matmul(x1)  # Compute the dot product of the dropout output and the value tensor

        return v3


# Initializing the model
m = Model()


