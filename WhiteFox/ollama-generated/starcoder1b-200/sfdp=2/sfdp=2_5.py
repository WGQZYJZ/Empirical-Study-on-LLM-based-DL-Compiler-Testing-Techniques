
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 512)
        self.key   = torch.nn.Linear(512, 512)
 
    def forward(self, query_input, key_input):
        qk = torch.matmul(query_input, key_input.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(float(self.key.weight.size(0)))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)
        value  = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

