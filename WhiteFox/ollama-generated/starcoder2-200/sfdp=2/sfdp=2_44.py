
class SelfAttention(torch.nn.Module):
    def __init__(self, input_features=512, key_features=640, dropout_p=0.1):
        super().__init__()
        self.key = torch.nn.Linear(input_features, key_features)
        self.query = torch.nn.Linear(input_features, key_features)
        self.value = torch.nn.Linear(input_features, input_features)

        self.dropout  = torch.nn.Dropout(p=dropout_p)

        self._scale  = (key_features // 32)**-0.5

    def forward(self, x):
        qk  = self.query(x).mul_(self._scale) 
        key  = self.key(x)
        value  = self.value(x)
 
        dropout_qk  = self.dropout(qk)
        scaled_qk  = torch.nn.functional.softmax(q * k, dim=-1)

        dropout_qk  = torch.nn.Dropout(dropout_p)(scaled_qk).mul_(value)
        return dropout_qk

m  = SelfAttention()

