
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(64, 8)
 
    def forward(self, qk1):
        softmax_qk1 = torch.softmax(qk1, dim=-1)
        dropout_qk1 = torch.nn.functional.dropout(softmax_qk1, p=dropout_p)
        output1 = dropout_qk1.matmul(v) # This line is added
        return output1


# Initializing the model
m = Model()


# Inputs to the model
q  = torch.randn(20, 3, 64, 64)
k = torch.randn(16, 3, 64, 64)
v = torch.randn(16, 3, 64, 64)
