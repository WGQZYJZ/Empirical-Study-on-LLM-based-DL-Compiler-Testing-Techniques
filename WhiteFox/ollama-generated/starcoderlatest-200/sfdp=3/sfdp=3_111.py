
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_k = torch.nn.Linear(128, 32, bias=False)
 
    def forward(self, x1, x2):
        qk = self.q_k(torch.cat([x1, x2], dim=-1))
        qk  = qk.transpose(-2, -1).reshape(-1, 32, 1, 1)
        softmax_qk = torch.nn.functional.softmax(qk, dim=-2)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.25)
        output = qk * dropout_qk
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 128)
x2 = torch.randn(32, 128)
