
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, key_mask=None):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(math.pi)
        if key_mask is None:
            softmax_qk = scaled_qk
        else:
            assert key_mask.size() == x2.shape  # Make sure that `key_mask` has the same shape as `value`.
            softmax_qk = torch.mul(scaled_qk, key_mask)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v = dropout_qk.matmul(x2)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
