
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(0.5 * 1 / math.sqrt(64))
        self.dropoutp = 0.2

    def forward(self, query_, key_value_, scale=None):
        scale = scale or self.scale
        qk = torch.matmul(query_, key_.transpose(-2, -1))
        scaled_qk = qk * scale_factor # compute the dot product of the query and key tensors
        softmax_qk = scaled_qk.softmax(dim=-1)  # apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropoutp)   # apply dropout to the softmax output
        output = dropout_qk.matmul(value_)  # compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model