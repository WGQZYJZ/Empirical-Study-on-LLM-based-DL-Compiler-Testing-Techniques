
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3072, 128)
        self.dropout = torch.nn.Dropout(p=dropout_p)
        self.linear2 = torch.nn.Linear(128, 64)
        self.linear3 = torch.nn.Linear(64, 46)
 
    def forward(self, x1):
        v = self.dropout(F.relu(self.linear1(x1)))
        return F.log_softmax(self.linear2(v), dim=-1)

# Initializing the model
m = Model()

# Inputs to the model
inputs  = torch.randn(batch, seq_len, hidden)
outputs  = m(inputs)
