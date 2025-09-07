
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 512)
        self.key = torch.nn.Linear(768, 512)
        self.value = torch.nn.Linear(768, 512)

    def forward(self, x):
        qk = torch.matmul(self.query(x), self.key.transpose(-2, -1)) / math.sqrt(math.sqrt(768 * 512))
        softmax_qk = F.softmax(qk, dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=0.5, training=self.training)
        output = torch.matmul(dropout_qk, self.value(x))
        return output


# Initializing the model
m = Model()


