
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(8, 1)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk = qk / (inv_scale_factor) 
        softmax_qk = torch.softmax(scaled_qk, dim=-1) 
        dropout_qk = F.dropout(softmax_qk, p=0.1, training=True) 
        output = dropout_qk.matmul(value)
        return self.fc(output)


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(256, 8, 32, 32)
key = torch.randn(256, 8, 32, 32)
value = torch.randn(256, 8, 64, 64)
