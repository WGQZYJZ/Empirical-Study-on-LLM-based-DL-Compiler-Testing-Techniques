
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(20, 10)
        self.key   = torch.nn.Linear(20, 10)
        self.value = torch.nn.Linear(10, 3)

    def forward(self, x):
        qk = torch.matmul(x, self.query)
        key_scale = (torch.pow(
            self.key.weight**2, -0.5))
        key_scale.mul_(self.value)
        key_scale.add_(1e-6) # Preventing numerical issues
        scaled_qk  = qk / key_scale
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        out = dropout_qk.matmul(self.value)
        return out


# Initializing the model
m = Model()


