
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 128)
        self.key = torch.nn.Linear(3072, 128)
        self.value = torch.nn.Linear(128, 128)

    def forward(self, x1):
        query = self.query(x1).view(-1, 768)
        key = self.key(x1).view(-1, 3072)
        value = self.value(x1).view(-1, 128)
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(self.key.weight.diag().unsqueeze(dim=0)).unsqueeze(dim=1).expand(q.shape[:-2] + (self.key.out_features,))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()


