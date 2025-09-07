
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self._query = torch.nn.Linear(32, 16)
        self._key = torch.nn.Linear(32, 8)
        self._value = torch.nn.Linear(32, 4)
        self._scale_factor = math.sqrt(32.)

        self._dropout = torch.nn.Dropout(0.5)

    def forward(self, query):
        
        key = self._key(query)
        value = self._value(query)

        qk = torch.matmul(
            self._query(query),
            key.transpose(-2, -1)) / math.sqrt(32.)

        scale_factor  = math.sqrt(32.)

        dropout_qk  =  torch.nn.functional.dropout(softmax_qk, p=0.5)

        output = dropout_qk @ value
        return output

# Initializing the model
m = AttentionModel()

 # Inputs to the model
x1 = torch.randn(32, 32)
 
__output__  = m(x1)
