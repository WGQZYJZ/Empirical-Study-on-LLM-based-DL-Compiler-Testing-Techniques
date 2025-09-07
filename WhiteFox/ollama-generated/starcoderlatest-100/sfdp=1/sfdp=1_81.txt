
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 128, bias=False)
 
    def forward(self, x1, x2):
        v1 = self.qkv(x1)
        qk, key, value = v1.split([64, 32, 32], dim=-1)
        qk = self._dropout(qk)
        key = self._dropout(key)
        value = self._dropout(value)

        qv = torch.matmul(qk, key.transpose(-2, -1))
        scaled_qv = qv.div(inv_scale_factor)
        softmax_qv = scaled_qv.softmax(dim=-1)
        output = softmax_qv.matmul(value)

        return output

    @staticmethod
    def _dropout(x):  # type: (torch.Tensor) -> torch.Tensor
        return x * (0.5 / (1 - dropout_p))

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
