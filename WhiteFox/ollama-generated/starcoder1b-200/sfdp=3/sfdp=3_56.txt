
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        # Input x1 is used to compute the dot product of q and k tensors, then scaled_qk
        # is multiplied by scale_factor in __init__ above.

        # The softmax function was applied in __init__, so it will return a tensor with shape (batch_size, seq_len, num_heads)
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(self.d_k)  # Compute the dot product of x1 and x2 tensors

        softmax_qk = qk.mul(self.scale_factor) / math.sqrt(self.d_k)  # Scale the dot product by a factor
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output

        y = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and x2 tensor

        return y


# Initializing the model
m = Model()


