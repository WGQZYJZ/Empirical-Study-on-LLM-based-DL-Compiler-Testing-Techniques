
class Model(torch.nn.Module):
    def __init__(self, key_depth, hidden_depth, query_depth):
        super().__init__()
        self.key_depth = key_depth
        self.hidden_depth = hidden_depth
        self.query_depth = query_depth
        self.key_linear = torch.nn.Linear(
            in_features=self.query_depth, out_features=self.key_depth)
        self.value_linear = torch.nn.Linear(
            in_features=self.query_depth, out_features=self.hidden_depth)
 
    def forward(self, query):
        key = self.key_linear(query).view(-1, self.key_depth, 1, 1)
        value = self.value_linear(query).view(-1, self.hidden_depth, 1, 1)
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output
 

# Inputs to the model
x1 = torch.randn(256, 3, 256, 64)
