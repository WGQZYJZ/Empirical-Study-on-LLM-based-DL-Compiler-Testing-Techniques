
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_qk = torch.nn.Linear(128, 36)
 
    def forward(self, query, key):
        qk = self.linear_qk(query * (1 / math.sqrt(1024)))
        softmax_qk = torch.nn.functional.softmax(qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3)
        output = dropout_qk @ key
        return output


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(64, 128)
key    = torch.randn(256, 128)
