
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
 
    def forward(self, x1, x2):
        q1 = self.linear(x1)
        q2 = self.linear(x2)
        scaled_qk = torch.matmul(q1, q2.transpose(-2, -1)) * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 128)
x2 = torch.randn(1, 32, 128)
