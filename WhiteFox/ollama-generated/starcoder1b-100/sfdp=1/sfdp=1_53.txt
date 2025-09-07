
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 6)
        self.key = torch.nn.Linear(3, 6)
        self.value = torch.nn.Linear(3, 6)
 
    def forward(self, query1, key1, value):
        qk = torch.matmul(query1, key1.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(self.key_dim)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m  = Model()


