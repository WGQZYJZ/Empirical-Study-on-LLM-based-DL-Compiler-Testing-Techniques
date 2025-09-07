
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 32)
        self.key = torch.nn.Linear(768, 16)
        self.value = torch.nn.Linear(512, 4)
 
    def forward(self, x):
        qk = torch.matmul(x, self.key.weight)
        scaled_qk = qk.mul(torch.exp(self.query.weight))
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x, self.value.weight)
        return output


# Initializing the model
m  = Model()
