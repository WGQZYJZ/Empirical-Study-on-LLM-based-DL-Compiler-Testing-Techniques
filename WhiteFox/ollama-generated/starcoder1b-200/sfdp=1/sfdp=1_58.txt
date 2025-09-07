
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(4096, 256)
        self.key = torch.nn.Linear(256, 128)
        self.value = torch.nn.Linear(128, 3)
 
    def forward(self, x1):
        qk = torch.matmul(self.query(x1), self.key.transpose(-2, -1))
        scaled_qk = qk.div(torch.sqrt(self.attention_scale))
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        dropout_qk = nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(self.value(x1))
        return output


# Initializing the model
m = Model()


