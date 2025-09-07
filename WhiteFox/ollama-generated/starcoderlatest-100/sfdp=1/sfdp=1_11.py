
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_layer = torch.nn.Linear(768, 3072)
        self.k_layer = torch.nn.Linear(768, 3072)
        self.v_layer = torch.nn.Linear(768, 3072)
 
    def forward(self, x1):
        v1 = self.q_layer(x1)
        v2 = self.k_layer(x1)
        v3 = self.v_layer(x1)
        qk = torch.matmul(v1, v2.transpose(-2, -1)) / math.sqrt(768 * 768)
        scaled_qk = qk.div(math.sqrt(24576))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v3)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 24576, 8, 8)
