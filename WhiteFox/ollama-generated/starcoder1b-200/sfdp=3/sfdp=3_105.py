
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 5)
        self.key   = torch.nn.Linear(20, 6)
        self.value = torch.nn.Linear(40, 8)

    def forward(self, x1):
        query  = self.query(x1)
        key    = self.key   (x1)
        value  = self.value (x1)

        # The dot product of query and key is scaled by a factor `1/sqrt(5)`
        # and then softmax function is applied to the output
        qk = torch.matmul(query, key.transpose(-2, -1)) / sqrt_constant
        qk_softmax = qk.mul(scale_factor)
        dropout_qk = torch.nn.functional.dropout(qk_softmax, p=dropout_p)
        value_output = dropout_qk.matmul(value)

        return value_output


# Initializing the model
m = Model()


