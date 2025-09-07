
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(10, 4)
        self.key = torch.nn.Linear(10, 5)
        self.value = torch.nn.Linear(20, 6)

    def forward(self, x1):
        q = self.query(x1)
        k = self.key(x1)
        v = self.value(x1)

        # Here we compute the scaled dot product of (q, k), then softmax is applied to (scaled_qk,),
        # then dropout is applied to both the scaled dot product and the scaled output (output).
        # The input `query` contains 10 tokens with their weights and biases, while the input `key` contains 5 tokens
        # with their weights and biases. After a multiplication by a constant, we get `scaled_qk`.
        scaled_qk = torch.matmul(q, k).div(torch.exp(2. * math.log10(-20000.) + 0.5))

        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)

        output = dropout_qk.matmul(v)
        return output


# Initializing the model
m = Model()

