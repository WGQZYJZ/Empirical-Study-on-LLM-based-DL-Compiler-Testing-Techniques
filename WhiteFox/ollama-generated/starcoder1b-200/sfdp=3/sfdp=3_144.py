
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 64)
        self.key   = torch.nn.Linear(3, 128)
        self.value = torch.nn.Parameter(torch.tensor([[0., 0.]]))
        self.scale_factor = torch.tensor([0.5])
        self.dropout_p = torch.nn.functional.dropout

    def forward(self, x, y):
        qk = torch.matmul(x, y.transpose(-2, -1)) * self.scale_factor
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(y)
        return output

# Initializing the model
m = Model()


